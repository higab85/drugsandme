# Generated by Django 2.0.7 on 2018-08-13 07:59

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0028_auto_20180809_1520'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articlecategory',
            name='name',
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='name_en',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='articlecategory',
            name='name_es',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='articlepage',
            name='colour',
            field=colorfield.fields.ColorField(default='#6c6c1c', max_length=18),
        ),
    ]
