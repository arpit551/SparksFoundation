from django.shortcuts import render
from donation.forms import donateform
from django.conf import settings
from django.shortcuts import redirect
import requests
from .models import Donations
#
#
# def homepage(request):
#     form=donateform()
#     return render(request,'home.html',{'form':form})
def donate(request):
    if request.method == 'POST':
        form=donateform(request.POST)

        if form.is_valid():
            headers = {"X-Api-Key": settings.INSTAMOJO_API, 'X-Auth-Token': settings.INSTAMOJO_AUTH}
            payloads = {
                'purpose': "Donation",
                'amount': form.data['DonationAmount'],
                'buyer_name': form.data['Name'],
                'email': form.data['Email'],
                'phone': '',
                'redirect_url': 'https://sparksfoundation.herokuapp.com/',
                'send_email': 'False',
                'send_sms': 'False',
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

            data = response.json()
            try:
                id = data['payment_request']['id']
            except:
                return render(request, 'home.html', {'form': form, 'paid_status': 'False'})
            f = form.save(commit=False)
            f.RequestId = id
            f.save()
            return redirect(data['payment_request']['longurl'])
        else:
            return render(request, 'home.html', {'form': form, 'paid_status': 'False'})


    else:
        form = donateform()
        request_id=request.GET.get('payment_request_id')
        if request_id is not None:
            donation=Donations.objects.get(RequestId=request_id)
            donation.PaymentStatus=True
            donation.save()
            return render(request, 'home.html', {'form': form,'paid_status':'True','donation':donation})
        return render(request, 'home.html', {'form': form,'paid_status':'False'})

