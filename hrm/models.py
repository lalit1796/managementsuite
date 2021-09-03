from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from model_utils import Choices
from enum import Enum
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# new job codes
class Job(models.Model):    
    Job_code = models.CharField(blank=True,null=True,unique=True,max_length=32,default=000,help_text="")
    Department = models.CharField(max_length=32,default="",help_text="")
    Designation = models.CharField(max_length=32,default="",help_text="")
    Ctc = models.CharField(max_length=32,default=0,help_text="Annual cost to company")
    Location = models.CharField(max_length=80,blank=True,null=True,default="",help_text="")
    Description = models.TextField(blank=True,null=True,default="",help_text="")
    Notes = models.TextField(blank=True,null=True,default="",help_text="")
    User_firm = models.CharField(max_length=32,blank=True,null=True,default="",help_text="")
    Job_firm_id = models.CharField(blank=True,null=True,max_length=32,default=0,help_text="")
    By = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET("USER IS REMOVED")) 
    
    
    
class Candidate(models.Model):

    gender = [
        ('male','Male'),
        ('female','Female'),
        ('other','Other'),
    ]
    married_status = [
        ('married','Married'),
        ('unmarried','Not Married'),
    ]
    
    #basic
    First_name = models.CharField(max_length=32,help_text="")
    Middle_name = models.CharField(max_length=32,blank=True,null=True,default="",help_text="")
    Last_name = models.CharField(max_length=32,help_text="")
    Father_name = models.CharField(max_length=32,help_text="")
    Mother_name = models.CharField(max_length=32,blank=True,null=True,default="",help_text="")
    Marital_status =  models.CharField(max_length=100,choices=married_status,default="Not Married",help_text="")
    Spouse_name = models.CharField(max_length=32,blank=True,null=True,help_text="")
    Date_of_birth = models.DateField(auto_now=False, auto_now_add=False,default="")
    Gender = models.CharField(max_length=100,choices=gender,default="Male",help_text="")
    Phone1 = models.CharField(max_length=10,help_text="")
    Phone2 = models.CharField(max_length=10,blank=True,null=True,default="",help_text="")
    Email = models.CharField(max_length=50,blank=True,null=True,help_text="")
    
    #Address 
    Current_address = models.CharField(max_length=200,help_text="")
    Current_address_pin = models.CharField(max_length=6,help_text="")
    Current_address_city = models.CharField(max_length=50,help_text="")
    Current_address_state = models.CharField(max_length=50,help_text="")
    Permanent_address = models.CharField(max_length=200,blank=True,null=True,default="",help_text="")
    Permanent_address_pin = models.CharField(max_length=6,blank=True,null=True,default="",help_text="")
    Permanent_address_city = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Permanent_address_state = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    
    #documents number
    Aadhaar_number = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    PAN_number = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Voter_id = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Passport = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Driver_license = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
     
    #emergency
    Emergency_contact_name = models.CharField(max_length=50,blank=True,null=True,help_text="")
    Emergency_contact_relation = models.CharField(max_length=50,blank=True,null=True,help_text="")
    Emergency_contact_phone1 = models.CharField(max_length=10,blank=True,null=True,help_text="")
    Emergency_contact_phone2 = models.CharField(max_length=10,blank=True,null=True,default="",help_text="")
    Emergency_contact_email = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Emergency_contact_address = models.CharField(max_length=200,blank=True,null=True,help_text="")
   
    
    By = models.ForeignKey(settings.AUTH_USER_MODEL,null=True,blank=True,on_delete=models.SET("USER IS REMOVED")) 
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)