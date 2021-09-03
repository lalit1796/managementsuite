from django.shortcuts import render
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

from .forms import employeeForm

# Create your views here.
def index_view(request,*args,**kwargs):
    
    data = serializers.serialize('json', Employee.objects.all(), fields=('pk','First_name'))
    response={
        
        'response': data,
        
    }
    return JsonResponse(response) 