from django.shortcuts import render
from donation.forms import donateform
from django.conf import settings
from django.shortcuts import redirect
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
            'redirect_url': 'https://sparksfoundation.herokuapp.com/',
            'send_email': 'False',
            'send_sms': 'True',
            'webhook': '',
            'allow_repeated_payments': 'False',
        }
        # payloads = {
        #     'purpose': "Donation",
        #     'amount': 45,
        #     'buyer_name': 'bc',
        #     'email': 'imarpit02@gmail.com',
        #     'phone': 8561842219,
        #     'redirect_url': 'https://sparksfoundation.herokuapp.com/',
        #     'send_email': 'False',
        #     'send_sms': 'True',
        #     'webhook': '',
        #     'allow_repeated_payments': 'False',
        # }

        response = requests.post("https://test.instamojo.com/api/1.1/payment-requests/", data=payloads,
                                 headers=headers)
        data=response.json()

        return redirect(data['payment_request']['longurl'])

    else:
        return render(request,'donation.html')

