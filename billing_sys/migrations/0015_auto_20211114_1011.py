# Generated by Django 3.2.8 on 2021-11-14 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_sys', '0014_alter_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='new_user',
            name='ph_no',
            field=models.CharField(max_length=10),
        ),
    ]
