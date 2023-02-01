from django.db import models


class Client(models.Model):
    first_name = models.CharField(blank=False, max_length=30)
    last_name = models.CharField(blank=True, max_length=30)
    reg_date = models.DateField(auto_now=True, blank=True)
