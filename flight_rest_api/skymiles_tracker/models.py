from django.db import models

# Create your models here.

class Airport(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=6)

class Deal(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    departure_airport = models.ForeignKey(Airport, on_delete=(models.CASCADE), related_name='departure_airport')
    arrival_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='arrival_airport')
    miles = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    
    def __repr__(self):
        return '{} -> {} for {}'.format(self.departure_airport, self.arrival_airport, self.miles)

    def __eq__(self, other):
        #forgive me father, for I have written a long if statement.... please auto format on save
        if self.arrival_airport == other.arrival_airport and self.departure_airport == other.departure_airport and self.miles == other.miles and self.start_date == other.start_date and self.end_date == other.end_date:
            return True
        else:
            return False
