# Generated by Django 2.0.9 on 2018-10-09 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_snippets', '0004_codesnippet_code_samples'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codesnippet',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
