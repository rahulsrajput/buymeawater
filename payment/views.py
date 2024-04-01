from django.shortcuts import render
from django.http import HttpResponseRedirect
from payment.models import Payment
from instamojo_wrapper import Instamojo
from django.conf import settings


api = Instamojo(api_key=settings.API_KEY, 
                auth_token=settings.AUTH_TOKEN,
                endpoint='https://test.instamojo.com/api/1.1/'
                )


# Create your views here.
def support(request):
    try:
        if request.user.is_authenticated:

            if request.method == 'POST':
                data = request.POST
                value = data.get('value')
                message = data.get('msg')
                amount = 20 * (int(value))
                email = request.user.email
                # print(email)

                payment_obj, created = Payment.objects.get_or_create(
                    user = request.user,
                    is_paid = False,
                )

                response = api.payment_request_create(
                    purpose=message,
                    amount=amount,
                    buyer_name=request.user,
                    email=email,
                    redirect_url='http://127.0.0.1:8000/support-success',
                    send_email=True,
                )
                # print(response)
                payment_obj.order_id=response['payment_request']['id']

                payment_obj.amount=response['payment_request']['amount']

                payment_obj.quantity = value

                payment_obj.save()

                context = {
                    'value':value,
                    'amount':amount,
                    'payment_long':response['payment_request']['longurl']
                }

            else:
                
                return HttpResponseRedirect('/')

        else:
            return HttpResponseRedirect('login/')
        return render(request, 'payment/payment.html', context)
    
    except Exception as e:
        print(e)



def supportSuccess(request):
    try:
        if request.user.is_authenticated:
            payment_request_id = request.GET.get('payment_request_id')
            payment_id = request.GET.get('payment_id')
            payment_status = request.GET.get('payment_status')
            # print(payment_id, payment_request_id)
            # print(payment_status)

            payment_obj = Payment.objects.get(order_id = payment_request_id)    
            
            if payment_status == 'Failed':
                return render(request, 'payment/paymentFailed.html')
                
            else:
                payment_obj.is_paid = True
                payment_obj.payment_id = payment_id
                payment_obj.status = payment_status
                payment_obj.save()

            
            context = {
                'payment_obj':payment_obj
                }
            return render(request, 'payment/paymentSuccess.html',context)
        
        else:
            return HttpResponseRedirect('login/')
    
    except Exception as e:
        print(e)