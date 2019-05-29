from django.db import models

# Create your models here.
class Donations(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    DonationAmount=models.IntegerField()
    PhoneNumber=models.CharField(max_length=10)

