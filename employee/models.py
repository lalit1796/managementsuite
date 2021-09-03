from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from model_utils import Choices
from enum import Enum
from datetime import datetime
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class Employee(models.Model):
    
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
    
    #bank
    Bank_name = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Account_number = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    IFSC_code = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    
    #job information
    Job_title = models.CharField(max_length=50,help_text="")
    Department = models.CharField(max_length=50,help_text="")
    Work_place = models.CharField(max_length=50,help_text="")
    Work_location = models.CharField(max_length=50,help_text="")
    Date_of_joining = models.DateField(auto_now=False, auto_now_add=False)
    Work_email = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Official_phone = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Reporting_officer = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    
    #emergency
    Emergency_contact_name = models.CharField(max_length=50,help_text="")
    Emergency_contact_relation = models.CharField(max_length=50,help_text="")
    Emergency_contact_phone1 = models.CharField(max_length=10,help_text="")
    Emergency_contact_phone2 = models.CharField(max_length=10,blank=True,null=True,default="",help_text="")
    Emergency_contact_email = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Emergency_contact_address = models.CharField(max_length=200,help_text="")
   
    #nominee
    Nominee_name = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Nominee_relation = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Nominee_contact_phone1 = models.CharField(max_length=10,blank=True,null=True,default="",help_text="")
    Nominee_contact_phone2 = models.CharField(max_length=10,blank=True,null=True,default="",help_text="")
    Nominee_contact_email = models.CharField(max_length=50,blank=True,null=True,default="",help_text="")
    Nominee_contact_address = models.CharField(max_length=200,blank=True,null=True,default="",help_text="")
    
    by = models.ForeignKey(settings.AUTH_USER_MODEL,models.SET("Manually"))
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True) 
    
    
    
    
    
    
class Customsetting(models.Model):    
    Code = models.CharField(max_length=32,blank=True,null=True,default="",help_text="")
    Name = models.CharField(max_length=32,blank=True,null=True,default="",help_text="")
    Setting = models.TextField(blank=True,null=True,default="",help_text="")