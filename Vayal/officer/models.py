from django.db import models


schem_type=[('Janakeeyasoothranam','Janakeeyasoothranam'),
            ('Department of agriculture','Department of agriculture')]

class Schem(models.Model):
    name=models.CharField(max_length=250)
    type=models.CharField(max_length=50,choices=schem_type)
    description=models.CharField(max_length=250)
    criteria=models.CharField(max_length=250)
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateField()

    def __str__(self):
        return self.name