from django.db import models

class Donations(models.Model):
    Name=models.CharField(max_length=30)
    Email=models.EmailField()
    DonationAmount=models.IntegerField()
    PhoneNumber=models.CharField(max_length=10)
    RequestId=models.CharField(max_length=100)
    PaymentStatus=models.BooleanField(default=False)

