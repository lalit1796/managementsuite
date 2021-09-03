# Generated by Django 2.2.2 on 2020-03-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='Married_status',
            new_name='Marital_status',
        ),
        migrations.AlterField(
            model_name='employee',
            name='Email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Emergency_contact_email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Emergency_contact_phone2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Father_name',
            field=models.CharField(default=0, max_length=32),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='Phone2',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
