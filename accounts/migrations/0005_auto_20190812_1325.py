# Generated by Django 2.2.2 on 2019-08-12 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20190812_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=100, unique=True, verbose_name='phone'),
        ),
    ]
