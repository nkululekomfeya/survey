from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
class Choice(models.Model):
    name= models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Poll(models.Model):
    name= models.CharField(max_length=200)
    choices= models.ManyToManyField(
        Choice, related_name='related_polls',blank=True
    )
    
    def __str__(self):
        return self.name
    
class Vote(models.Model):
    poll = models.ForeignKey(
        Poll, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    choice = models.ForeignKey(
        Choice, on_delete=models.SET_NULL, related_name="votes", null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.poll.name} - {self.choice.name}"