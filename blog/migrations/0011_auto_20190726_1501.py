# Generated by Django 2.1.5 on 2019-07-26 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181014_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpage',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage'),
        ),
    ]
