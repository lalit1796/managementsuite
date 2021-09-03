from django.shortcuts import render, redirect
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required 

# Create your views here.
def home_view(request,*args,**kwargs):
    
    context={
        
        
    }
    return render(request,"home.html",context)
    
def logout_view(request):
    logout(request)
    return redirect('home')    
    
    
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')
        next = request.POST.get('next','')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            
            if next is not '':
                return HttpResponseRedirect(next)
            else:
                return redirect('home')
        else:
            return redirect('home')  
    else:
        return redirect('home')
        
 
#settings
@login_required(login_url='/')
def settings_view(request,*args,**kwargs):
   
    
    context={
        
        
        
    }
    return render(request,"settings.html",context)