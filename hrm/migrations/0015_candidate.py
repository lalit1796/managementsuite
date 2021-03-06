# Generated by Django 2.2.2 on 2020-05-31 11:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('hrm', '0014_job_job_firm_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=32)),
                ('Middle_name', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('Last_name', models.CharField(max_length=32)),
                ('Father_name', models.CharField(max_length=32)),
                ('Mother_name', models.CharField(blank=True, default='', max_length=32, null=True)),
                ('Marital_status', models.CharField(choices=[('married', 'Married'), ('unmarried', 'Not Married')], default='Not Married', max_length=100)),
                ('Spouse_name', models.CharField(blank=True, max_length=32, null=True)),
                ('Date_of_birth', models.DateField(default='')),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], default='Male', max_length=100)),
                ('Phone1', models.CharField(max_length=10)),
                ('Phone2', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('Email', models.CharField(blank=True, max_length=50, null=True)),
                ('Current_address', models.CharField(max_length=200)),
                ('Current_address_pin', models.CharField(max_length=6)),
                ('Current_address_city', models.CharField(max_length=50)),
                ('Current_address_state', models.CharField(max_length=50)),
                ('Permanent_address', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('Permanent_address_pin', models.CharField(blank=True, default='', max_length=6, null=True)),
                ('Permanent_address_city', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Permanent_address_state', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Aadhaar_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('PAN_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Voter_id', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Passport', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Driver_license', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Emergency_contact_name', models.CharField(blank=True, max_length=50, null=True)),
                ('Emergency_contact_relation', models.CharField(blank=True, max_length=50, null=True)),
                ('Emergency_contact_phone1', models.CharField(blank=True, max_length=10, null=True)),
                ('Emergency_contact_phone2', models.CharField(blank=True, default='', max_length=10, null=True)),
                ('Emergency_contact_email', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('Emergency_contact_address', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('by', models.ForeignKey(on_delete=models.SET('Manually'), to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
