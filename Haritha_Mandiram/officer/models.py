from django.db import models

# Create your models here.

gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')
    ]
land_ownership=[
    ('own','own'),
    ('lease','lease')
    ]

panchayath=[('Feroke','Feroke')]

district=[('Kozhikode','Kozhikode')]

benefinting=[
    ('Yes','Yes'),
    ('No','No')
    ]



class HM_User(models.Model):
    name=models.CharField(max_length=225)
    dob=models.DateField()
    genter= models.CharField(max_length=20, choices=gender)
    phone_number = models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=225,unique=True)
    password=models.CharField(max_length=8)
    conform_password=models.CharField(max_length=8)
    def __str__(self):
        return self.name


class Schem(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    criteria=models.CharField(max_length=100)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()
    def __str__(self):
        return self.name


class Notification(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    attachment = models.FileField(upload_to='notifications/', blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
