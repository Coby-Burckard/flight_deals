from django.db import models

# Create your models here.

class Deal(models.Model):
    date_created = models.DateField()
    date_removed = models.DateField()
    active = models.BooleanField(null=False)

    class Meta():
        ordering = ['-date_created']

    def __repr__(self):
        pass

    def __eq__(self, other):
        cities = self.Airport_set.all()
        if cities in other.Airport_set.all():
            return True
        else:
            return False
        pass

class Airport(models.Model):
    deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
    name = models.CharField(max_length = 10)