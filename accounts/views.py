import json as simplejson 
from django.shortcuts import render
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import redirect
from employee.models import Employee, Customsetting
from hrm.models import Job, Candidate
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required  
from django.template.loader import render_to_string, get_template
from django.middleware import csrf


from employee.forms import employeeForm # this form is in employee app..., Any changes there will be shown here...
#from .forms import jobForm, newCandidateForm

# Create your views here.
@login_required(login_url='/')
def index_view(request,*args,**kwargs):
    
    context={
        
        
    }
    return render(request,"accounts/index.html",context)

#billDesk
@login_required(login_url='/')
def bill_desk_view(request,*args,**kwargs):
    
    context={
        
        
    }
    return render(request,"accounts/billDesk.html",context)
    
##jax for billDesk  
##tools
@login_required(login_url='/') 
def billDesk_tools_jax(request,*args,**kwargs):
   
   
    
    context={
       
     
        
    }
    html = render_to_string("accounts/billDesk_jax/tools.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

###generate_bill    
@login_required(login_url='/') 
def billDesk_new_bill_jax(request,*args,**kwargs):
   
   
    
    context={
       
     
        
    }
    html = render_to_string("accounts/billDesk_jax/new_bill.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 
    
    
def billDesk_bill_info_jax(request,*args,**kwargs):
   
    #data = serializers.serialize('json', Jon.objects.all())
    response={
							
		"template":"lalsdti",
			"company":{
				"name":"asdf",
				"gst":None,
				"pan":None,
				"address":"",
				"unit":""
				},
			"client":{
				"name":"sdggdg",
				"gst":None,
				"pan":None,
				"address":"asdffdf",
				"unit":None
				},
				"logo":"url",
                "footer":True,
				"inwords":True,
				"heads":["serial","services","qty","days","rate","amount"],
                "type":["number","text","number","number","number","number"],
                "disabled":["disabled","","","","","disabled"],
				"formula":"a*b*c*d=e",
				"items" : [[1,"housekeeping",454,200,5454,545468],[2,"gda",454,200,5454,545468]]
						
					}
    return JsonResponse(response)
    
    
    
#Accounting
@login_required(login_url='/')
def acc_desk_view(request,*args,**kwargs):
    
    context={
        
        
    }
    return render(request,"accounts/accounting.html",context)
    
##jax for Accounting 
    