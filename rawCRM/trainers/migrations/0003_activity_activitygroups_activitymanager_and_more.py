# Generated by Django 4.1.5 on 2023-02-20 23:31

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainers', '0002_crew'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityGroups',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ActivityManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='client',
            name='birth_date',
            field=models.DateField(blank=True, default=datetime.date(2023, 1, 1)),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(default='qwerty', max_length=30),
        ),
        migrations.CreateModel(
            name='Parents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.CharField(blank=True, max_length=30)),
                ('email', models.CharField(blank=True, max_length=30)),
                ('telephone', models.CharField(blank=True, max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.client')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(default='123', max_length=30)),
                ('street', models.CharField(default='123', max_length=30)),
                ('house', models.CharField(blank=True, max_length=30)),
                ('building', models.CharField(blank=True, max_length=30)),
                ('flat', models.CharField(blank=True, max_length=30)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainers.client')),
            ],
        ),
    ]
