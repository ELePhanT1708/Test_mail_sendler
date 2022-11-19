# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Subscriber(models.Model):
    name = models.CharField(max_length=180)
    email = models.EmailField()
    birthdate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Subscriber'
