# Generated by Django 2.2.2 on 2020-05-27 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0013_auto_20200527_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='Job_firm_id',
            field=models.CharField(blank=True, default=0, max_length=32, null=True),
        ),
    ]
