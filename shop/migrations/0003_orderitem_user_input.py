# Generated by Django 2.2.2 on 2019-07-17 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_orderitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitem',
            name='user_input',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
