# Generated by Django 3.2.15 on 2022-09-30 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agroapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_tb',
            old_name='Email',
            new_name='EMAIL',
        ),
        migrations.RenameField(
            model_name='register_tb',
            old_name='Name',
            new_name='NAME',
        ),
        migrations.RenameField(
            model_name='register_tb',
            old_name='Password',
            new_name='PASSWORD',
        ),
    ]
