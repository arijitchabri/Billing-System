# Generated by Django 3.2.8 on 2021-11-13 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_sys', '0008_check'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.BooleanField()),
            ],
        ),
    ]
