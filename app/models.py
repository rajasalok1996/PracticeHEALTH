# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Roles(models.Model):
    role = models.CharField(max_length=50)
    def __str__(self):
        return self.role

class Person(models.Model):
    user = models.OneToOneField(User)
    phone_no = models.CharField(null=False,max_length=15)
    emergency_contact = models.CharField(null=False,max_length=15)
    age = models.PositiveIntegerField()
    # guardian = models.ForeignKey('self',null=True)
    # person_role = models.ManyToManyField(Roles)


class Amenity(models.Model):
    amenity = models.CharField(max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=50)


class Hospital(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    amenity = models.ManyToManyField(Amenity)
    department = models.ManyToManyField(Department)


