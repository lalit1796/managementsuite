from django.shortcuts import render
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

# Create your views here.
def index_view(request,*args,**kwargs):
    
    context={
        
        
    }
    return render(request,"crm/index.html",context)