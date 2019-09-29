# Generated by Django 2.0 on 2019-09-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(choices=[('en', 'English'), ('ru', 'Russian')], default='ru', max_length=20, verbose_name='Language'),
        ),
    ]
