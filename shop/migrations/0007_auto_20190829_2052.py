# Generated by Django 2.2.2 on 2019-08-29 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_pagetext_text_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Order', 'verbose_name_plural': 'Orders'},
        ),
        migrations.AlterModelOptions(
            name='pagetextgroup',
            options={'verbose_name': 'Page text', 'verbose_name_plural': 'Page text'},
        ),
    ]
