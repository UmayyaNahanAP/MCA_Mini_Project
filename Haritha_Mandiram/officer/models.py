from django.db import models
from django.core.exceptions import ValidationError
from PIL import Image

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

def validate_image(image):
    filesize = image.file.size
    max_megabyte_size = 30.0  # Set maximum file size (30MB in this example)

    if filesize > max_megabyte_size * 1024 * 1024:
        raise ValidationError(f"Max file size is {max_megabyte_size}MB")

    # Validate image dimensions
    # img = Image.open(image)
    # max_width, max_height = 1024, 1024  # Set maximum dimensions (e.g., 1024x1024)
    # if img.width > max_width or img.height > max_height:
    #     raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels")


class SchemApplication(models.Model):
    schem_name=models.CharField(max_length=225)
    name=models.CharField(max_length=50)
    dob=models.DateField()
    gender = models.CharField(max_length=20,choices=gender)
    house_name = models.CharField(max_length=255)
    village = models.CharField(max_length=255)
    panchayath = models.CharField(max_length=100,choices=panchayath)
    district = models.CharField(max_length=100,choices=district)
    pincode = models.CharField(max_length=6)
    contact_no=models.CharField(max_length=10)
    email=models.EmailField()
    land_ownership= models.CharField(max_length=50,choices=land_ownership)
    land_area = models.CharField(max_length=255)
    survay_no= models.CharField(max_length=5)
    benefinting=models.CharField(max_length=10,choices=benefinting)
    bank_name=models.CharField(max_length=255)
    branch=models.CharField(max_length=255)
    account_no=models.CharField(max_length=19)
    ifsc_code=models.CharField(max_length=11)
    photo=models.ImageField(upload_to='documents/photo/', validators=[validate_image])
    sign=models.ImageField(upload_to='documents/sign/')
    aadhar=models.ImageField(upload_to='documents/aadhar/')
    land_tax=models.ImageField(upload_to='documents/land_tax/')
    bank_pass=models.ImageField(upload_to='documents/bank_pass/')
    
    def __str__(self):
        return self.name
