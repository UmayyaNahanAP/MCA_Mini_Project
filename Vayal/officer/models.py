from django.db import models
from django.contrib.auth.models import User


schem_type=[('Janakeeyasoothranam','Janakeeyasoothranam'),
            ('Department of agriculture','Department of agriculture')]



class Scheme(models.Model):
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