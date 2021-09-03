from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from .models import Employee, Customsetting
import csv 
from django.http import HttpResponse
from django.template.defaultfilters import slugify
from django.db import models



class CsvImportForm(forms.Form):
    csv_file = forms.FileField()
    
class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export selected"   
    
    
    
    
    

    
    
admin.site.register(Employee)
admin.site.register(Customsetting)
    