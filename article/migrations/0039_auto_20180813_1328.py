# Generated by Django 2.0.7 on 2018-08-13 13:28

import article.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0038_auto_20180813_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesectionen',
            name='section_addons',
            field=wagtail.core.fields.StreamField([('effects', wagtail.core.blocks.StructBlock([('positive_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('neutral_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('negative_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))])), ('content', wagtail.core.blocks.RichTextBlock(blank=True)), ('table_of_three', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_1', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_2', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_2', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_3', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_3', wagtail.core.blocks.RichTextBlock(blank=True))])), ('interactions', wagtail.core.blocks.StructBlock([('interactions', wagtail.core.blocks.ListBlock(article.models.Interaction))])), ('brain_tip', wagtail.core.blocks.StructBlock([('click_the_brain_text', wagtail.core.blocks.CharBlock(blank=True, default='Click the brain for neuro-info!', max_length=255)), ('content', wagtail.core.blocks.RichTextBlock(blank=True))]))], blank=True),
        ),
        migrations.AlterField(
            model_name='articlesectiones',
            name='section_addons',
            field=wagtail.core.fields.StreamField([('effects', wagtail.core.blocks.StructBlock([('positive_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('neutral_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('negative_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))])), ('content', wagtail.core.blocks.RichTextBlock(blank=True)), ('table_of_three', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_1', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_2', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_2', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_3', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_3', wagtail.core.blocks.RichTextBlock(blank=True))])), ('interactions', wagtail.core.blocks.StructBlock([('interactions', wagtail.core.blocks.ListBlock(article.models.Interaction))])), ('brain_tip', wagtail.core.blocks.StructBlock([('click_the_brain_text', wagtail.core.blocks.CharBlock(blank=True, default='Click the brain for neuro-info!', max_length=255)), ('content', wagtail.core.blocks.RichTextBlock(blank=True))]))], blank=True),
        ),
    ]
