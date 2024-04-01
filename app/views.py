from django.shortcuts import render, redirect
from payment.models import Payment


# Create your views here.
def buymeWater(request):
    try:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return redirect('dashboard/')
            else:
                return render(request, 'app/home.html')
        else:
            return redirect('/login')

    
    except Exception as e:
        print(e)


def supportHistory(request):
    try:
        order_id = request.GET.get('order-id')

        if order_id is not None:
            objs = Payment.objects.filter(order_id__icontains = order_id, user=request.user)
        else:
            objs = Payment.objects.filter(user=request.user)
            

        credits = Payment.objects.filter(status='Credit', user=request.user)
        # print(credits)
        total_amount = 0
        for credit in credits:
            # print(obj.amount)
            total_amount += credit.amount

        context = {
            'objs':objs,
            'total_amount':total_amount
        }
        return render(request, 'app/supporthistory.html', context)

    
    except Exception as e:
        print(e)



def dashboard(request):
    try:
        order_id = request.GET.get('order-id')

        if order_id is not None:
            objs = Payment.objects.filter(order_id__icontains = order_id)
        else:
            objs = Payment.objects.filter(status='Credit')

        
        credits = Payment.objects.filter(status='Credit')
        # print(credits)
        total_amount = 0
        for credit in credits:
            # print(obj.amount)
            total_amount += credit.amount

        context = {
            'objs':objs,
            'total_amount':total_amount
        }
        return render(request, 'app/dashboard.html', context)

    
    except Exception as e:
        print(e)