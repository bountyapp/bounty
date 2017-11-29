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
    store_name = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    by_when = models.CharField(max_length= 20)
    destination = models.CharField(max_length=200)
    reward = models.CharField(max_length=200)
    progress = models.CharField(max_length=100)
    review_cus = models.CharField(max_length=200)
    review_del = models.CharField(max_length=200)

    def __str__(self):
        return self.item

