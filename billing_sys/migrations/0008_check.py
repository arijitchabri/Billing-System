# Generated by Django 3.2.8 on 2021-11-13 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing_sys', '0007_alter_new_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chicken_65', models.BooleanField()),
                ('paneer_pakora', models.BooleanField()),
                ('biryani', models.BooleanField()),
                ('chicken_hundi', models.BooleanField()),
                ('jeera_rice', models.BooleanField()),
                ('mutton_kosha', models.BooleanField()),
                ('special_rajasthani_thali', models.BooleanField()),
                ('ramen', models.BooleanField()),
                ('rosogolla', models.BooleanField()),
                ('keshar_lassi', models.BooleanField()),
                ('butter_scotch', models.BooleanField()),
                ('rainbow_mousse', models.BooleanField()),
            ],
        ),
    ]