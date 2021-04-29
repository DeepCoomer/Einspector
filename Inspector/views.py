from django.shortcuts import render
from Inspector.models import Fir
from Inspector.models import Contact
from Inspector.models import StatusDetails
import requests
from .form import *
from django.contrib import messages

# Create your views here.


def index(request):
    query_params = {
        "source": "The Times of India",
        "sortBy": "top",
        "apiKey": "d65ec3df76b0482bade20e7c2b295d08"
    }
    main_url = "https://newsapi.org/v2/top-headlines?country=in"

    res = requests.get(main_url,params=query_params)
    top = res.json()
    l = top['articles']
    desc =[]
    news =[]
  
    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
    mylist = zip(news, desc)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phoneno = request.POST.get('phoneno')
        Report = request.POST.get('Report')
        index = Contact(name=name,email=email,phoneno=phoneno,Report=Report)
        index.save()
    
    return render(request,'index.html',context={"mylist":mylist})

def fir(request):
    if request.method == 'POST':
        form = FirForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request,messages.SUCCESS,'Your Fir has been Registered Successfully,You can Track your fir by checking the FIR Status on the homepage of the website.')
    else:
        form = FirForm()
    return render(request,'Fir.html',{'form':form})

def status(request):
    return render(request,'Status.html')

def statusdetails(request):
    if request.method == 'POST':
        Name = request.POST.get('name')
        Addhar = request.POST.get('addhar')
        statusdetails = StatusDetails(Name=Name,Addhar=Addhar)
        statusdetails.save()
        info = Fir.objects.get(Addhar=Addhar)
        print(info.Name,info.Address,info.City,info.State,info.Pincode,info.Firdescription,info.Date,info.Time,info.Status)
        context = {
            'Name':info.Name,
            'Address':info.Address,
            'City':info.City,
            'State':info.State,
            'Pincode':info.Pincode,
            'AddharNumber':info.Addhar,
            'FirDescription':info.Firdescription,
            'Date':info.Date,
            'Time':info.Time,
            'FirStatus':info.Status
        }
    return render(request, 'Statusdetails.html',context)
