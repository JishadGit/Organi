# Generated by Django 3.2.15 on 2022-11-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agroapp', '0012_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='QUANTITY',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]