from django.db import models
import datetime
from django.utils import timezone

class Member(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    def __unicode__(self):
        return self.username

class Poll(models.Model):
    question = models.CharField(max_length=200)
    author = models.ForeignKey(Member)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
from django.db import models
import datetime
from django.utils import timezone

class Member(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

class Poll(models.Model):
    question = models.CharField(max_length=200)
    author = models.ForeignKey(Member)
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.question
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    poll = models.ForeignKey(Poll)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.choice_text
