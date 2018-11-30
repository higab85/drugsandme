# Generated by Django 2.1 on 2018-11-30 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0061_auto_20181130_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='articleconstants',
            old_name='cookie_banner_en',
            new_name='cookie_banner_message_en',
        ),
        migrations.RenameField(
            model_name='articleconstants',
            old_name='cookie_banner_es',
            new_name='cookie_banner_message_es',
        ),
        migrations.AddField(
            model_name='articleconstants',
            name='cookie_banner_button_en',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='articleconstants',
            name='cookie_banner_button_es',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='articleconstants',
            name='cookie_banner_link_en',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='articleconstants',
            name='cookie_banner_link_es',
            field=models.URLField(blank=True),
        ),
    ]
