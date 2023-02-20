from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    reg_date = models.DateField(auto_now=True, blank=True)
    birth_date = models.DateField(auto_now=False, blank=True)

class Address(models.Model):
    city = models.CharField(blank=False)
    street = models.CharField(blank=False)
    house = models.CharField(blank=True)
    building = models.CharField(blank=True)
    flat = models.CharField(blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Parents(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    name = models.CharField(blank=True, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=30)
    telephone = models.CharField(blank=True, max_length=30)


class Activity(models.Model):
    pass

class ActivityGroups(models.Model):
    pass

class ActivityManager(models.Model):
    pass




class Crew(User):
    pass