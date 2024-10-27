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

schem_type = [('Janakeeyasoothranam','Janakeeyasoothranam'),
            ('Department of agriculture','Department of agriculture')]

benefiting=[('Yes','Yes'),
             ('No','No')]

scheme_status = [('Pending', 'Pending'),
                 ('Approved', 'Approved'),
                 ('Rejected', 'Rejected')]

complaint_status = [('Pending', 'Pending'),
                    ('In Progress', 'In Progress'),
                    ('Resolved', 'Resolved'),
                    ('Unresolvable', 'Unresolvable')]

class Agricultural_officer(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    phone_number = models.CharField(max_length=10)
    unique_code = models.CharField(max_length=10)
    def __str__(self):
        return self.name


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
    

class Scheme(models.Model):
    officer=models.ForeignKey(Agricultural_officer, on_delete=models.CASCADE)
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=50,choices=schem_type)
    description=models.CharField(max_length=250)
    criteria=models.CharField(max_length=250)
    cast_eligibility = models.CharField(max_length=50,choices=cast,default='All')
    land_ownership=models.CharField(max_length=20, choices=land,default='All')
    posted_date=models.DateTimeField(auto_now_add=True)
    start_date=models.DateField()
    end_date=models.DateField()

    def __str__(self):
        return self.name
    
    
class SchemeApplication(models.Model):
    scheme=models.ForeignKey(Scheme, on_delete=models.CASCADE)
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    officer=models.ForeignKey(Agricultural_officer, on_delete=models.CASCADE)
    benefiting=models.CharField(max_length=50,choices= benefiting)
    house_number= models.CharField(max_length=250)
    ward_number= models.CharField(max_length=250)
    total_land_area = models.CharField(max_length=255)
    land_survay_no= models.CharField(max_length=5)
    bank_name=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    account_no=models.CharField(max_length=19)
    sign=models.ImageField(upload_to='scheme/sign/')
    aadhar=models.FileField(upload_to='scheme/aadhar/')
    land_tax=models.FileField(upload_to='scheme/land_tax/')
    bank_pass=models.FileField(upload_to='scheme/bank_pass/')
    applied_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=scheme_status, default='Pending')
    def __str__(self):
        return f"{self.vayal_user} - {self.scheme}"
    

class VegetablePermission(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    officer=models.ForeignKey(Agricultural_officer, on_delete=models.CASCADE)
    farm_name = models.CharField(max_length=250)
    farm_place = models.CharField(max_length=250)
    total_land_area = models.CharField(max_length=255)
    land_survay_no= models.CharField(max_length=5)
    sign=models.ImageField(upload_to='vegetable_permission/sign/')
    aadhar= models.FileField(upload_to='vegetable_permission/aadhar/')
    land_tax= models.FileField(upload_to='vegetable_permission/land_tax/')
    applied_date=models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=vegetable_permission_status, default='Pending')

    def __str__(self):
        return  f"{self.vayal_user} - {self.farm_name}"
    
class Vegetable(models.Model):
    farm_details = models.ForeignKey(VegetablePermission, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    quantity =  models.IntegerField()
    expiry =  models.IntegerField()
    posted_date=models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='vegetables')
    def __str__(self):
        return  f"{self.farm_details.vayal_user} - {self.farm_details.farm_name} - {self.name}"

class VegetablePurchase(models.Model):
    vayal_user =models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    vegetable = models.ForeignKey(Vegetable, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.vayal_user.name} - {self.vegetable.name}"
    

class Complaint(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=complaint_status, default='Pending')

    def __str__(self):
        return self.title
    
class Notification(models.Model):
    vayal_user = models.ForeignKey(Vayal_User,null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    date =models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class LeaseLand(models.Model):
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    land_name= models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    period=models.IntegerField()
    land_lease_rent = models.IntegerField()
    posted_date=models.DateTimeField(auto_now_add=True)
    photo=models.ImageField(upload_to='photo/')
    def __str__(self):
        return self.land_name
