from django.shortcuts import render
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse
from django.http import JsonResponse
from employee.models import Employee, Customsetting
from django.core import serializers
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.decorators import login_required, permission_required 


# Create your views here.
@login_required(login_url='/')
def index_view(request,*args,**kwargs):
    
    context={
        
        'sign':'home',
    }
    return render(request,"register/register_home_page.html",context)
    
@login_required(login_url='/')    
def new_register_view(request,*args,**kwargs):
    employee = Employee.objects.all()
    context={
        
       'emp':employee,
       'sign':'new',
    }
    return render(request,"register/new_register.html",context)
    
@login_required(login_url='/')   
def all_register_view(request,*args,**kwargs):
    
    context={
        
        'sign':'view',
        
    }
    return render(request,"register/all_register.html",context)
    
    
#JSON

@login_required(login_url='/')
@csrf_protect
def unassigned_employee_json(request,*args,**kwargs):
    
    data = serializers.serialize('json', Employee.objects.all(), fields=('pk','First_name'))
    response={
        
        'response': data,
        
    }
    return JsonResponse(response)    