# Generated by Django 2.1 on 2018-11-30 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0062_auto_20181130_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articleconstants',
            name='cookie_banner_message_en',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='articleconstants',
            name='cookie_banner_message_es',
            field=models.TextField(blank=True),
        ),
    ]
