# Generated by Django 2.2.2 on 2020-05-27 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0012_auto_20200526_1254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='by',
            new_name='By',
        ),
        migrations.RenameField(
            model_name='job',
            old_name='user_firm',
            new_name='User_firm',
        ),
        migrations.AlterField(
            model_name='job',
            name='Job_code',
            field=models.CharField(blank=True, default=0, max_length=32, null=True, unique=True),
        ),
    ]
