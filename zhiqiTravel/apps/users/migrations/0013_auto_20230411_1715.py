# Generated by Django 2.1.2 on 2023-04-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20230323_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='check_time',
            field=models.DateField(default='2023-01-01', verbose_name='签到时间'),
        ),
    ]
