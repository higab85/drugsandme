# Generated by Django 2.0.9 on 2018-10-08 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0021_image_file_hash'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogindexpage',
            name='intro',
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='sub_title_en',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='sub_title_es',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_en',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='blogindexpage',
            name='title_es',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='cover_image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='sub_title',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
