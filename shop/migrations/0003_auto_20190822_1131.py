# Generated by Django 2.2.2 on 2019-08-22 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190822_1126'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pagetext',
            old_name='page',
            new_name='group',
        ),
    ]
