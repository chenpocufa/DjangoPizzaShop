# Generated by Django 2.2.2 on 2019-08-29 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timetable', '0004_auto_20190829_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='weekday',
            field=models.CharField(choices=[('5', 'Friday'), ('3', 'Wednesday'), ('2', 'Tuesday'), ('7', 'Sunday'), ('6', 'Saturday'), ('1', 'Monday'), ('4', 'Thursday')], max_length=1, verbose_name='Day of the week'),
        ),
    ]
