# Generated by Django 3.2.4 on 2022-04-09 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_alter_signup_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='About',
            field=models.CharField(max_length=450, null=True),
        ),
    ]
