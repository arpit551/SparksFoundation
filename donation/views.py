from django.shortcuts import render
from donation.forms import donateform
from django.conf import settings
import requests


def homepage(request):
    form=donateform()
    return render(request,'home.html',{'form':form})
def donatesubmit(request):
    if request.method == 'POST':
        form=donateform(request.POST)

        form.save()
        headers = {"X-Api-Key": settings.INSTAMOJO_API, 'X-Auth-Token': settings.INSTAMOJO_AUTH}
        payloads = {
            'purpose': "Donation",
            'amount': form.data['DonationAmount'],
            'buyer_name': form.data['Name'],
            'email': form.data['Email'],
            'phone': form.data['PhoneNumber'],
            'redirect_url': '',
            'send_email': 'True',
            'send_sms': 'True',
            'webhook': '',
            'allow_repeated_payments': 'False',
        }
        response = requests.post("https://test.instamojo.com/api/1.1/payment-requests/", data=payloads,
                                 headers=headers)
        return render(request, 'donation.html', {'response': response,'y':'yes'})

    else:
        return render(request,'donation.html')

