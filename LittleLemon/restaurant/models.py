from django.db import models
from django.utils.timezone import now

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField(null=False)
    BookingDate = models.DateTimeField(default = now)
    
    def __str__(self): 
        return self.Name


# Add code to create Menu model
class Menu(models.Model):
   Title = models.CharField(max_length=255) 
   price = models.DecimalField(max_digits=5, decimal_places=2)
   inventory = models.IntegerField(null=False) 

   def __str__(self):
      return self.Title