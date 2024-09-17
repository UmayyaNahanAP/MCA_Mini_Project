from django.db import models

# Create your models here.

class Schem(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    criteria=models.CharField(max_length=100)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()
    def __str__(self):
        return self.name