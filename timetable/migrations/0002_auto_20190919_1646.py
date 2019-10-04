# Generated by Django 2.0 on 2019-09-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='weekday',
            field=models.CharField(choices=[('1', 'Monday'), ('2', 'Tuesday'), ('7', 'Sunday'), ('3', 'Wednesday'), ('5', 'Friday'), ('4', 'Thursday'), ('6', 'Saturday')], max_length=1, verbose_name='Day of the week'),
        ),
    ]
