import json as simplejson 
from django.shortcuts import render
from pytz import timezone
from datetime import datetime,timedelta
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.shortcuts import redirect
from employee.models import Employee, Customsetting
from .models import Job, Candidate
from django.core import serializers
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required  
from django.template.loader import render_to_string, get_template
from django.middleware import csrf


from employee.forms import employeeForm # this form is in employee app..., Any changes there will be shown here...
from .forms import jobForm, newCandidateForm

# Create your views here.
@login_required(login_url='/')
def index_view(request,*args,**kwargs):
   
    
    context={
        
        'sign':'home',
        
    }
    return render(request,"hrm/announcement.html",context)
    
#employee 
@login_required(login_url='/')
def employee_view(request,*args,**kwargs):
    employee = Employee.objects.all()
    set = Customsetting.objects.get(Code = 'view')
    
    context={
       
        'sign':'empl',
        'emp':employee, 
        'set':set,
       
        
    }
    return render(request,"hrm/employee.html",context)

@login_required(login_url='/')
def employee_new_add_view (request,*args,**kwargs):
    addNewEmployeeform = employeeForm(request.POST or None)
    
    if not addNewEmployeeform.is_valid():
        form = addNewEmployeeform 
        
    else:
        inst = addNewEmployeeform.save()
        id=str(inst.id)
        form = employeeForm(None)
        return redirect("id/"+id)
    
    context={
        'sign':'empl',
        'form':form
        
    }
    return render(request,"hrm/employee_n1_addNew.html",context)

@login_required(login_url='/') 
def employee_profile_view(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
        
    }
    return render(request,"hrm/employee_n1_id.html",context) 
    
 ##jax for emplpoyee 
@login_required(login_url='/') 
def employee_profile_basic_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/basic.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

@login_required(login_url='/')    
def employee_profile_emergency_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/emergency.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

@login_required(login_url='/')    
def employee_profile_employement_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/employement.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')     

@login_required(login_url='/')
def employee_profile_family_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/family.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

def employee_profile_nominee_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/nominee.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')

def employee_profile_documents_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/documents.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')

def employee_profile_job_jax(request,id,*args,**kwargs):
    
    employee = Employee.objects.get(pk=id)
       
    context={
        
        'sign':'empl',
        'emp' : employee
    }
   
    html = render_to_string("hrm/employee_n1_id_jax/job.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')    
    
    
    
#recruit
@login_required(login_url='/') 
def recruit_view(request,*args,**kwargs):
   
    
    context={
       
        'sign':'recr',
        
       
        
    }
    return render(request,"hrm/recruit.html",context)

@login_required(login_url='/')    
def recruit_vacancy_view(request,*args,**kwargs):
   
    new_job = Job.objects.all()
    
    context={
       
        'sign':'recr',
        'jobs':new_job,
        
       
        
    }
    return render(request,"hrm/recruit_n1_vacancy.html",context)   

@login_required(login_url='/')    
def recruit_vacancy_new_view(request,*args,**kwargs):
    
    company_code_session = "sfms"
    
    print(request.method)
    if request.method == 'POST': #redirecting to avoid resubmitting on refresh.
        path = request.get_full_path()
        job_code_form = jobForm(request.POST)
        if job_code_form.is_valid():
            count = Job.objects.filter(User_firm=company_code_session).count()
            
           
            inst = job_code_form.save(commit=False)
            inst.by = request.user
            inst.User_firm = company_code_session;
            if count == 0:
                inst.Job_firm_id = 1   
            else: 
                latest = Job.objects.filter(User_firm=company_code_session).order_by('-Job_code')[0]
                inst.Job_firm_id = int(latest.Job_firm_id) + 1
            
            inst.Job_code =  company_code_session + str(inst.Job_firm_id)
            inst.save()
            id=str(inst.id)
            context={
                'sign':'recr',
                
            }
            return redirect(path+"?created="+id)
        else:
            job_code_form = jobForm(request.POST)
            print("no")
            context={
               
                'sign':'recr',
                'form': job_code_form,
             
            }
            return render(request,"hrm/recruit_n1_vacancy_n2_new_job_code.html",context)
    elif request.method == 'GET': 
        status = request.GET.get('created',None) 
        
        if status is not None:
            new_job = Job.objects.get(pk = status)
            context={
               
                'sign':'recr',
                'created':True,
                'job':new_job,
               
                
            }
            return render(request,"hrm/recruit_n1_vacancy_n2_new_job_code.html",context)
        else:
            job_code_form = jobForm(None)
            context={
                'sign':'recr',
                'form': job_code_form,
            }
            return render(request,"hrm/recruit_n1_vacancy_n2_new_job_code.html",context)
                
    
    else: # this seems to run never but still there!... bcoz request is either get or post
        job_code_form = jobForm(None)
        context={
            'sign':'recr',
        }
        return render(request,"hrm/recruit_n1_vacancy_n2_new_job_code.html",context)



@login_required(login_url='/') 
def recruit_hire_view(request,*args,**kwargs):
    job = Job.objects.all()
    
    context={
       
        'sign':'recr',
        'jobs':job,
       
        
    }
    return render(request,"hrm/recruit_n1_hire.html",context)


@login_required(login_url='/') 
def recruit_hire_code_view(request,code,*args,**kwargs):
    job = Job.objects.get(Job_code=code)
    employee = Employee.objects.all()
    set = Customsetting.objects.get(Code = 'view')
    
    context={
       
        'sign':'recr',
        'cod':job,
        'emp' : employee
       
        
    }
    return render(request,"hrm/recruit_n1_hire_n2_code.html",context)

##jax for recruit   
@login_required(login_url='/') 
def recruit_hire_code_candidates_jax(request,*args,**kwargs):
   
    employee = Candidate.objects.all().order_by('-id')
    set = Customsetting.objects.get(Code = 'view')
    
    context={
       
       
       
        "emp" : employee
       
        
    }
    html = render_to_string("hrm/recruit_n1_hire_n2_code_jax/candidates.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json') 

def recruit_hire_code_newcandidates_jax(request,*args,**kwargs):
   
    addNewCandidateform = newCandidateForm(request.POST or None)
    
    if not addNewCandidateform.is_valid():
        form = addNewCandidateform 
        
    else:
        inst = addNewCandidateform.save(commit=False)
        inst.By = request.user
        inst.save()
        id=str(inst.id)
        form = newCandidateForm(None) #just to make sure form is emptied...
        
        msg = "<h3><center>Candidate is saved with id "+id+"<center></h3>"
        serialized_data = simplejson.dumps({"html": msg})
        return HttpResponse(serialized_data, content_type='application/json')
    
    context={
        
        'form':form,
        'csrf':csrf.get_token(request),
        
    }
    
    html = render_to_string("hrm/recruit_n1_hire_n2_code_jax/newcandidates.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')     


def recruit_hire_code_stats_jax(request,*args,**kwargs):
   
    addNewEmployeeform = employeeForm(request.POST or None)
    
    
    
    context={
        
        
        'csrf':csrf.get_token(request),
        
    }
    
    html = render_to_string("hrm/recruit_n1_hire_n2_code_jax/stats.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')

def recruit_hire_code_edit_jax(request,*args,**kwargs):
   
    addNewEmployeeform = employeeForm(request.POST or None)
    
    
    
    context={
        
        
        'csrf':csrf.get_token(request),
        
    }
    
    html = render_to_string("hrm/recruit_n1_hire_n2_code_jax/edit.html", context)
    serialized_data = simplejson.dumps({"html": html})
    return HttpResponse(serialized_data, content_type='application/json')
    
#payroll 
@login_required(login_url='/') 
def payroll_view(request,*args,**kwargs):

    employee = Employee.objects.all()
    set = Customsetting.objects.get(Code = 'view') # will be use for different payroll table structure setting // meanwhile view setting
    
    context={
       
        'sign':'payr',
        'emp':employee, 
        'set':set,
       
        
    }
    return render(request,"hrm/payroll.html",context)
 
@login_required(login_url='/') 
def create_paysheet_view(request,*args,**kwargs):

    employee = Employee.objects.all()
    set = Customsetting.objects.get(Code = 'view') # will be use for different payroll table structure setting // meanwhile view setting
    
    context={
       
        'sign':'payr',
        'emp':employee, 
        'set':set,
       
        
    }
    return render(request,"hrm/payroll_n1_createSalary.html",context)
    
#training
@login_required(login_url='/')
def training_view(request,*args,**kwargs):
   
    
    context={
        
        'sign':'trai',
        
    }
    return render(request,"hrm/training.html",context)
    
    
#file
@login_required(login_url='/')
def file_view(request,*args,**kwargs):
   
    
    context={
        
        'sign':'file',
        
    }
    return render(request,"hrm/file.html",context)
    
#report
@login_required(login_url='/')
def report_view(request,*args,**kwargs):
   
    
    context={
        
        'sign':'repo',
        
    }
    return render(request,"hrm/report.html",context)
    
    
    
#jax
@login_required(login_url='/')
def empl_code_data_jax(code,request,*args,**kwargs):
   
    data = serializers.serialize('json', Jon.objects.all())
    response={
        
        'response': data,
        
    }
    return JsonResponse(response)