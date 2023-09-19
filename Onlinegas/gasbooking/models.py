from django.db import models

class Client_details(models.Model):
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=255)


class Admin_details(models.Model):
    username = models.CharField(max_length=255, unique=True)
    fullname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    mobile_no = models.BigIntegerField()
    address = models.CharField(max_length=255)