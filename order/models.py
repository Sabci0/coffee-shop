from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,blank=True)
    def __str__(self):
        return f'{self.name}'

class UserDetail(models.Model):
    zipcode = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)
    address = models.CharField(max_length=200)


    def __str__(self):
        return self.username