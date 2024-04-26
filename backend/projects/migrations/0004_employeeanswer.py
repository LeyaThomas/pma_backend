# Generated by Django 5.0.4 on 2024-04-26 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_projectemployee'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mark', models.IntegerField(default=0)),
                ('answer1', models.BooleanField(default=False)),
                ('answer2', models.BooleanField(default=False)),
                ('answer3', models.BooleanField(default=False)),
                ('answer4', models.BooleanField(default=False)),
                ('answer5', models.BooleanField(default=False)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.cususer')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
