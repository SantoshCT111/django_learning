from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request): 
    context ={ 'page':'aboutpage'}

    peoples = [
       {'name' : 'santosh chhetri ','age':'24'} ,
        {'name' : 'sandeep chhetri ','age':'20'} ,
         {'name' : 'sapana chhetri ','age':'28'} ,
          {'name' : 'sanju chhetri ','age':'26'} ,
    ]
    return render(request,"home/index.html", context={'peoples':  peoples,'page':context})

def aboutpage(request):
    context ={ 'page':'aboutpage'}
    return render(request, 'home/about.html',context)


def contactpage(request):
    context ={ 'page':'contact'}
    return render(request,'home/contact.html',context)