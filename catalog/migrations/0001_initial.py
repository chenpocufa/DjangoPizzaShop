# Generated by Django 2.2.2 on 2019-08-11 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=300)),
                ('photo', models.ImageField(upload_to='images/')),
                ('category', models.ManyToManyField(to='catalog.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('small', 'Small'), ('large', 'Large')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=5)),
                ('active', models.BooleanField(default=False)),
                ('pizza', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sizes', to='catalog.Pizza')),
            ],
        ),
    ]
