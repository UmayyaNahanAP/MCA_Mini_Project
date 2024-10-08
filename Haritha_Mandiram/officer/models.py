from django.db import models
from django.contrib.auth.models import User

# Create your models here.

gender=[
    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other')]

schem_type=[('Janakeeyasoothranam','Janakeeyasoothranam'),
            ('Department of agriculture','Department of agriculture')]

status=[
    ('Pending','Pending'),
    ('In Progress','In Progress'),
    ('Resolved','Resolved'),
    ('Unresolvable','Unresolvable')]

land_ownership=[
    ('own','own'),
    ('lease','lease')]

panchayath=[('Feroke','Feroke')]

district=[('Kozhikode','Kozhikode')]

benefinting=[
    ('Yes','Yes'),
    ('No','No')
    ]



class HM_User(models.Model):
    account = models.OneToOneField(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=225)
    dob=models.DateField()
    genter= models.CharField(max_length=20, choices=gender)
    phone_number = models.CharField(max_length=10)
    # def create_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         # print("create",sender, instance,created,**kwargs)
    #         HM_User.objects.create(user=instance)
    # def save_user_profile(sender, instance, **kwargs):
    #     # print("save",sender, instance,**kwargs)
    #     instance.profile.save()

    def __str__(self):
        return self.name

# def validate_image(image):
#     filesize = image.file.size
#     max_megabyte_size = 30.0  # Set maximum file size (30MB in this example)

#     if filesize > max_megabyte_size * 1024 * 1024:
#         raise ValidationError(f"Max file size is {max_megabyte_size}MB")

    # Validate image dimensions
    # img = Image.open(image)
    # max_width, max_height = 1024, 1024  # Set maximum dimensions (e.g., 1024x1024)
    # if img.width > max_width or img.height > max_height:
    #     raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels")


# class SchemApplication(models.Model):
#    # schem=models.ForeignKey(Schem,on_delete=models.CASCADE)
#     name=models.CharField(max_length=225)
#     dob=models.DateField()
#     gender = models.CharField(max_length=20,choices=gender)
#     house_name = models.CharField(max_length=255)
#     village = models.CharField(max_length=255)
#     panchayath = models.CharField(max_length=100,choices=panchayath)
#     district = models.CharField(max_length=100,choices=district)
#     pincode = models.CharField(max_length=6)
#     contact_no=models.CharField(max_length=10)
#     email=models.EmailField()
#     land_ownership= models.CharField(max_length=50,choices=land_ownership)
#     land_area = models.CharField(max_length=255)
#     survay_no= models.CharField(max_length=5)
#     benefinting=models.CharField(max_length=10,choices=benefinting)
#     bank_name=models.CharField(max_length=255)
#     branch=models.CharField(max_length=255)
#     account_no=models.CharField(max_length=19)
#     ifsc_code=models.CharField(max_length=11)
#     photo=models.ImageField(upload_to='documents/photo/')
#     #, validators=[validate_image])
#     sign=models.ImageField(upload_to='documents/sign/')
#     aadhar=models.ImageField(upload_to='documents/aadhar/')
#     land_tax=models.ImageField(upload_to='documents/land_tax/')
#     bank_pass=models.ImageField(upload_to='documents/bank_pass/')
    
#     def __str__(self):
#         return self.name


class VegitablePermissionForm(models.Model):
    name_of_the_applicant = models.CharField(max_length=225)
    dob = models.DateField()
    genter = models.CharField(max_length=20, choices=gender)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=225)
    farm_name = models.CharField(max_length=225)
    location_of_farm = models.URLField(max_length=250)
    photo = models.ImageField(upload_to='vegitable_form/photo/')
    sign = models.ImageField(upload_to='vegitable_form/sign/')
    declaration = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name_of_the_applicant
    

class Vegitable(models.Model):
    name = models.CharField(max_length=225)
    quantity = models.IntegerField()
    price= models.DecimalField(max_digits=10,decimal_places=2)
    posted_date=models.DateTimeField(auto_now_add=True)
    expiry = models.IntegerField()

    def __str__(self):
        return self.name


class Schem(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=50,choices=schem_type)
    description=models.CharField(max_length=250)
    criteria=models.CharField(max_length=250)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()

    def __str__(self):
        return self.name


class Notification(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    # attachment = models.FileField(upload_to='notifications/', blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    

class Complaint(models.Model):
    hm_user = models.ForeignKey(HM_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=status, default='Pending')

    def __str__(self):
        return self.title
