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
