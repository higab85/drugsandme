# Generated by Django 2.0.7 on 2018-08-06 11:23

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.snippets.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0016_auto_20180805_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesection',
            name='section_addons',
            field=wagtail.core.fields.StreamField([('effects', wagtail.core.blocks.StructBlock([('positive_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('neutral_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('negative_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))])), ('content', wagtail.core.blocks.RichTextBlock(blank=True)), ('table_of_three', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_1', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_2', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_2', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_3', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_3', wagtail.core.blocks.RichTextBlock(blank=True))])), ('interactions', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('drug_name', wagtail.core.blocks.CharBlock(blank=True, max_length=13)), ('interaction_type', wagtail.snippets.blocks.SnippetChooserBlock('article.InteractionType')), ('description', wagtail.core.blocks.RichTextBlock(blank=True))])))], blank=True),
        ),
    ]
