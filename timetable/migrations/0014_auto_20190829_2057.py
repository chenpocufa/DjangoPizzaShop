# Generated by Django 2.2.2 on 2019-08-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0013_auto_20190829_2053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='weekday',
            field=models.CharField(choices=[('4', 'Thursday'), ('6', 'Saturday'), ('3', 'Wednesday'), ('2', 'Tuesday'), ('1', 'Monday'), ('5', 'Friday'), ('7', 'Sunday')], max_length=1, verbose_name='Day of the week'),
        ),
    ]
