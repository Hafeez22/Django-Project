from typing import NamedTuple
from django.shortcuts import redirect, render
from .models import firstreview, items, review, tsm
from django.contrib import messages

# Create your views here.
def index(request):
    lists = items.objects.all()
    frev = firstreview.objects.all() 
    rev = review.objects.all()
    return render(request, 'index.html', {'lists': lists,'frevs': frev, 'revs': rev,})  

def submit(request):
    if(request.method == 'POST'):    
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST ['phone'] 
        text = request.POST['text'] 

        if tsm.objects.filter(email=email).exists():
            messages.info(request, 'You already Messaged')
            return redirect('/')
        elif tsm.objects.filter(phone=phone).exists():
            messages.info(request, 'You already Messaged')
            return redirect('/')    
        else:    
            record = tsm()
            record.name=name
            record.email=email
            record.phone=phone
            record.text=text
            record.save()

            message = "Thank You For Contacting Us"
            return redirect('/', {'message':message}) 
    else:
        return render(request, 'index.html')      