# Generated by Django 3.2.8 on 2021-11-10 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_sys', '0003_auto_20211108_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.IntegerField(verbose_name='What is the price'),
        ),
    ]
