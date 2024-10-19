from django.db import models
from django.contrib.auth.models import User


gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')]

cast=[('General','General'),
    ('OBC','OBC'),
    ('OEC','OEC')]


land=[('Own','Own'),
        ('Lease','Lease')]


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
    photo=models.ImageField(upload_to='documents/photo/')
    def __str__(self):
        return self.name
    



# class Vayal_User(models.Model):
#     account = models.OneToOneField(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=225)
#     dob=models.DateField()
#     genter= models.CharField(max_length=20, choices=gender)
#     phone_number = models.CharField(max_length=10)
#     aadhar_number= models.CharField(max_length=12)
#     cast=models.CharField(max_length=20, choices=cast)
#     house_name=models.CharField(max_length=225)
#     place=models.CharField(max_length=225)
#     village=models.CharField(max_length=225)
#     panchayat_muncipality_corporation=models.CharField(max_length=225)
#     district=models.CharField(max_length=225,default="Kozhikode")
#     pincode = models.CharField(max_length=6)
#     house_number= models.CharField(max_length=10)
#     ward_number=models.CharField(max_length=3)
#     land_ownership=models.CharField(max_length=20, choices=land)
#     total_land_area=models.CharField(max_length=225)
#     land_survay_number=models.CharField(max_length=225)
#     photo=models.ImageField(upload_to='documents/photo/')
#     def __str__(self):
#         return self.name
    

# class Vayal_User(models.Model):
#     account = models.OneToOneField(User, on_delete=models.CASCADE)
#     name=models.CharField(max_length=225)
#     dob=models.DateField()
#     genter= models.CharField(max_length=20, choices=gender)
#     phone_number = models.CharField(max_length=10)
#     aadhar_number= models.CharField(null=True,max_length=12)
#     cast=models.CharField(null=True,max_length=20, choices=cast)
#     house_name=models.CharField(null=True,max_length=225)
#     place=models.CharField(null=True,max_length=225)
#     village=models.CharField(null=True,max_length=225)
#     panchayat_muncipality_corporation=models.CharField(null=True,max_length=225)
#     district=models.CharField(null=True,max_length=225,default="Kozhikode")
#     pincode = models.CharField(null=True,max_length=6)
#     house_number= models.CharField(null=True,max_length=10)
#     ward_number=models.CharField(null=True,max_length=3)
#     land_ownership=models.CharField(null=True,max_length=20, choices=land)
#     total_land_area=models.CharField(null=True,max_length=225)
#     land_survay_number=models.CharField(null=True,max_length=225)
#     photo=models.ImageField(null=True,upload_to='documents/photo/')
#     def __str__(self):
#         return self.name