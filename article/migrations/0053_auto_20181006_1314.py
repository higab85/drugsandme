# Generated by Django 2.0.9 on 2018-10-06 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0052_auto_20181006_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactiontype',
            name='name_en',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='interactiontype',
            name='name_es',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
