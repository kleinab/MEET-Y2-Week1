from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<poll_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/vote/
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    # ex: /polls/5/results/
    url(r'^(?P<poll_id>\d+)/results/$', views.results, name='results'),
    # ex: /polls/add/
    url(r'^add/$', views.add, name='add'),
    # ex: /polls/save/
    url(r'^save/$', views.save, name='save'),
    # ex: /polls/login/
    url(r'^login/$', views.login, name='login'),
    # ex: /polls/login_post/
    url(r'^login_post/$', views.login_post, name='login_post'),
    # ex: /polls/signup/
    url(r'^signup/$', views.signup, name='signup'),
    # ex: /polls/signup_post/
    url(r'^signup_post/$', views.signup_post, name='signup_post'),
    # ex: /polls/logout/
    url(r'^logout/$', views.logout, name='logout'),
    
)

