from django.db import models
from django.contrib.auth.models import User


gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')]


class Vayal_User(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    dob=models.DateField()
    genter= models.CharField(max_length=20, choices=gender)
    phone_number = models.CharField(max_length=10)

    def __str__(self):
        return self.name