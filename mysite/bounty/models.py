from django.db import models
import datetime
# Create your models here.

class Quest(models.Model):
    customer = models.CharField(max_length=20, default='-')
    deliver = models.CharField(max_length=20, default='-')
    contents = models.CharField(max_length=200, default='-')
    places = models.CharField(max_length=200, default='-')
    destination = models.CharField(max_length=200, default='-')
    due = models.CharField(max_length= 20, default=datetime.datetime.now())
    cost = models.FloatField(max_length=20, default=0)
    reward = models.FloatField(max_length=20, default=0)
    total = models.FloatField(max_length=20, default=0)
    comments = models.CharField(max_length=100, default='-')
    status = models.CharField(max_length=100, default='waiting')
    confirm_cus = models.BooleanField(default=False)
    confirm_del = models.BooleanField(default=False)
    review_cus = models.CharField(max_length=200, default='-')
    review_del = models.CharField(max_length=200, default='-')
    score_cus = models.IntegerField(default=0)
    score_del = models.IntegerField(default=0)
    create_date = models.DateTimeField(max_length=20, default=datetime.datetime.now())
    complete_date = models.DateTimeField(max_length=20, default=datetime.datetime.now())

    def __str__(self):
        return self.contents



