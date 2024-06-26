# Generated by Django 5.0.3 on 2024-04-01 20:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiwako',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saxeli_qartulad', models.CharField(max_length=50)),
                ('saxeli_inglisurad', models.CharField(max_length=50)),
                ('fasi', models.FloatField()),
                ('photo', models.ImageField(upload_to='wiwakebi/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.category')),
            ],
        ),
    ]
