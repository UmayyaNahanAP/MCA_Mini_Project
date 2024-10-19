from django.db import models
from vayal_user.models import Vayal_User


complaint_status = [('Pending', 'Pending'),
                    ('In Progress', 'In Progress'),
                    ('Resolved', 'Resolved'),
                    ('Unresolvable', 'Unresolvable')]

schem_type = [('Janakeeyasoothranam','Janakeeyasoothranam'),
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