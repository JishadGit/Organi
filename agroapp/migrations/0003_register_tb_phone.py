# Generated by Django 3.2.15 on 2022-10-11 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroapp', '0002_auto_20220930_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='register_tb',
            name='PHONE',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
