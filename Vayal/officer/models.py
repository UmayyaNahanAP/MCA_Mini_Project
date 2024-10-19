from django.db import models
from vayal_user.models import Vayal_User

class Notification(models.Model):
    # cast = models.CharField(max_length=20, choices=Vayal_User.cast)
    vayal_user = models.ForeignKey(Vayal_User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    description = models.TextField()
    # attachment = models.FileField(upload_to='notifications/', blank=True, null=True)
    date = models.DateField()
    published = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title