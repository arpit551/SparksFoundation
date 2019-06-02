from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Donations(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    DonationAmount=models.IntegerField(validators=[ MinValueValidator(20)],verbose_name="Donation Amount (INR)")
    RequestId=models.CharField(max_length=100)
    PaymentStatus=models.BooleanField(default=False)

