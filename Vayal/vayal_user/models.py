from django.db import models
from django.contrib.auth.models import User


gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')]

cast=[('General','General'),
    ('OBC','OBC'),
    ('SC/ST','SC/ST')]

land=[('Own','Own'),
        ('Lease','Lease')]

vegetable_permission_status = [('Pending', 'Pending'),
                               ('Approved', 'Approved'),
                               ('Rejected', 'Rejected')]

class Vayal_User(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    dob=models.DateField()
    gender= models.CharField(max_length=20, choices=gender)
    phone_number = models.CharField(max_length=10)
    aadhar_number= models.CharField(max_length=12)
    cast=models.CharField(max_length=20, choices=cast)
    house_name=models.CharField(max_length=225)
    place=models.CharField(max_length=225)
    village=models.CharField(max_length=225)
    pincode = models.CharField(max_length=6)
    muncipality=models.CharField(max_length=225,default="Kozhikode")
    district=models.CharField(max_length=225,default="Kozhikode")
    land_ownership=models.CharField(max_length=20, choices=land)
    photo=models.ImageField(upload_to='photos/')
    joined_date=models.DateTimeField(auto_now_add=True)
    vegetable_permission_applied=models.CharField(max_length=225,default="False")
    vegetable_permission=models.CharField(max_length=225, choices=vegetable_permission_status,default="Pending")
    def __str__(self):
        return self.name
    

class LeaseLand(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    land_name= models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    period=models.IntegerField()
    land_lease_rent = models.IntegerField()
    photo=models.ImageField(upload_to='photo/')
    def __str__(self):
        return self.land_name
