from django.db import models

from django.db import models
from vayal_user.models import Vayal_User
from django.utils import timezone
import datetime


complaint_status = [('Pending', 'Pending'),
                    ('In Progress', 'In Progress'),
                    ('Resolved', 'Resolved'),
                    ('Unresolvable', 'Unresolvable')]

vegetable_permission_status = [('Pending', 'Pending'),
                               ('Approved', 'Approved'),
                               ('Rejected', 'Rejected')]

scheme_status = [('Pending', 'Pending'),
                 ('Approved', 'Approved'),
                 ('Rejected', 'Rejected')]

schem_type = [('Janakeeyasoothranam','Janakeeyasoothranam'),
            ('Department of agriculture','Department of agriculture')]

benefiting=[('Yes','Yes'),
             ('No','No')]

class Scheme(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=50,choices=schem_type)
    description=models.CharField(max_length=250)
    criteria=models.CharField(max_length=250)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()

    def __str__(self):
        return self.name

class SchemeApplication(models.Model):
    scheme=models.ForeignKey(Scheme, on_delete=models.CASCADE)
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    benefiting=models.CharField(max_length=50,choices= benefiting)
    house_number= models.CharField(max_length=250)
    ward_number= models.CharField(max_length=250)
    total_land_area = models.CharField(max_length=255)
    land_survay_no= models.CharField(max_length=5)
    bank_name=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    account_no=models.CharField(max_length=19)
    sign=models.ImageField(upload_to='sign/')
    aadhar=models.ImageField(upload_to='aadhar/')
    land_tax=models.ImageField(upload_to='land_tax/')
    bank_pass=models.ImageField(upload_to='bank_pass/')
    applied_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=scheme_status, default='Pending')
    def __str__(self):
        return str(self.scheme)


class VegetablePermission(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=250)
    farm_place = models.CharField(max_length=250)
    applied_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=vegetable_permission_status, default='Pending')

    def __str__(self):
        return self.farm_name

class Vegetable(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    farm_details = models.ForeignKey(VegetablePermission, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    quantity =  models.IntegerField()
    expiry =  models.IntegerField()
    posted_date=models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='vegetables')
    def __str__(self):
        return self.name 


class Complaint(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=complaint_status, default='Pending')

    def __str__(self):
        return self.title


class Notification(models.Model):
    # cast = models.CharField(max_length=20, choices=Vayal_User.cast)
    vayal_user = models.ForeignKey(Vayal_User,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    # attachment = models.FileField(upload_to='notifications/', blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title