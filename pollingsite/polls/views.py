from django.shortcuts import render
from polls.models import Choice, Poll

def index(request):
    latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)

def detail(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    return render(request, 'polls/detail.html', {'poll': poll})

def vote(request, poll_id):
    poll = Poll.objects.get(id=poll_id)
    if 'choice' not in request.POST: # User didn't make a choice
        return detail(request, poll_id)
    else:
        selected_choice = poll.choice_set.get(id=request.POST['choice'])
        selected_choice.votes += 1
        selected_choice.save()
        return index(request)
