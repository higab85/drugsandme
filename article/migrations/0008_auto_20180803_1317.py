# Generated by Django 2.0.7 on 2018-08-03 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_footerlink_socialmedia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialmedia',
            name='logo',
            field=models.CharField(max_length=255),
        ),
    ]
