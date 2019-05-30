from  django import forms
from django.forms import ModelForm
from donation.models import Donations

class donateform(ModelForm):
    class Meta:
        model=Donations
        fields=['Name','Email','DonationAmount','PhoneNumber']

