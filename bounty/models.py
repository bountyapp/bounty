from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=20)
    requested_num = models.IntegerField(default=0)
    fulfillment = models.IntegerField(default=0)
    distance_traveled = models.FloatField(default=0)

    def __str__(self):
        return self.name

class Quest(models.Model):
    customer = models.CharField(max_length=20)
    deliver = models.CharField(max_length=20)
    content = models.CharField(max_length=200)
    places = models.CharField(max_length=200)
    destination = models.CharField(max_length=200)
    by_when = models.DateTimeField(max_length= 20)
    cost = models.CharField(max_length=20)
    reward = models.CharField(max_length=20)
    progress = models.CharField(max_length=100)
    review_cus = models.CharField(max_length=200)
    review_del = models.CharField(max_length=200)

    def __str__(self):
        return self.item

