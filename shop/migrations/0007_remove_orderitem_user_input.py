# Generated by Django 2.2.2 on 2019-07-17 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_auto_20190717_0440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='user_input',
        ),
    ]
