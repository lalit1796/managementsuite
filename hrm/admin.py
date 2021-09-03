from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from employee.models import Employee, Customsetting
from .models import Job
import csv 
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.db import models

admin.site.register(Job)