# Generated by Django 2.2.2 on 2020-05-25 10:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0007_auto_20200525_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='by',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('USER IS REMOVED'), to=settings.AUTH_USER_MODEL),
        ),
    ]
