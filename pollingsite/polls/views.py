from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from polls.models import Choice, Poll, Member
from django.utils import timezone

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=poll_id))

def results(request, poll_id):
    poll = get_object_or_404(Poll, pk=poll_id)
    return render(request, 'polls/results.html', {'poll': poll})

def add(request):
    return render(request, 'polls/add.html')

def save(request):
    if 'member_id' not in request.session:
        return login(request)
    member_id = request.session['member_id']
    author = Member.objects.get(id=member_id)
    p = Poll(question=request.POST['question'], author=author, pub_date=timezone.now())
    p.save()
    p.choice_set.create(choice_text=request.POST['choice1'], votes=0)
    p.choice_set.create(choice_text=request.POST['choice2'], votes=0)
    p.choice_set.create(choice_text=request.POST['choice3'], votes=0)
    p.save()
    return HttpResponseRedirect(reverse('polls:index'))

def login(request):
    error_message = ""
    context = {'error_message' : error_message}
    return render(request, 'polls/login.html', context)

def login_post(request):
    m = Member.objects.filter(username=request.POST['username'])
    if len(m) == 0:
        error_message = "Username does not exist!"
        context = {'error_message': error_message}
        return render(request, 'polls/login.html', context)
    member = m[0]
    if member.password != request.POST['password']:
        error_message = "Invalid password!"
        context = {'error_message': error_message}
        return render(request, 'polls/login.html', context)
    else:
        request.session['member_id'] = member.id
        return index(request)

def signup(request):
    error_message = ""
    context = {'error_message': error_message}
    return render(request, 'polls/signup.html', context)

def signup_post(request):
    username = request.POST['username']
    password0 = request.POST['password0']
    password1 = request.POST['password1']
    if (password0 == password1):
        member = Member(username=username, password=password0)
        member.save()
        request.session['member_id'] = member.id
        return index(request)
    else:
        error_message = "Mismatch Passwords!"
        context = {'error_message': error_message}
        return render(request, 'polls/signup.html', context)

def logout(request):
    if 'member_id' in request.session:
        del request.session['member_id']
    return login(request)
