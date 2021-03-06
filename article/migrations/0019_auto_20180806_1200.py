# Generated by Django 2.0.7 on 2018-08-06 12:00

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('article', '0018_auto_20180806_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticlePageTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='articlepage',
            name='categories',
        ),
        migrations.AddField(
            model_name='articlepagetag',
            name='content_object',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='tagged_items', to='article.ArticlePage'),
        ),
        migrations.AddField(
            model_name='articlepagetag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_articlepagetag_items', to='taggit.Tag'),
        ),
    ]
