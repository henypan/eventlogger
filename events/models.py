import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=100)
    pub_date = models.DateTimeField('date published', default=datetime.datetime.now, blank=True)
    number = models.IntegerField('Number')
    difficulty = models.CharField(max_length=30)
    method = models.CharField(max_length=30, default='', blank=True)
    note = models.CharField(max_length=200, default='', blank=True)
    frequencies = models.IntegerField('Frequencies', default=0)
    
    def __unicode__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Pubished recenlty?'
