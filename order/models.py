from django.db import models

class User(models.Model):
    name = models.CharField(max_length=64)
    password = models.CharField(max_length=64,blank=True)
    def __str__(self):
        return f'{self.name}'

