# Generated by Django 2.0.9 on 2018-10-02 20:03

import article.models
from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0046_auto_20180925_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlesectionen',
            name='section_addons',
            field=wagtail.core.fields.StreamField([('effects', wagtail.core.blocks.StructBlock([('positive_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('neutral_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('negative_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))])), ('content', wagtail.core.blocks.RichTextBlock(blank=True)), ('table_of_three', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_1', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_2', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_2', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_3', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_3', wagtail.core.blocks.RichTextBlock(blank=True))])), ('interactions', wagtail.core.blocks.StructBlock([('interactions', wagtail.core.blocks.ListBlock(article.models.Interaction))])), ('brain_tip', wagtail.core.blocks.StructBlock([('click_the_brain_text', wagtail.core.blocks.CharBlock(blank=True, default='Click the brain for neuro-info!', max_length=255)), ('content', wagtail.core.blocks.RichTextBlock(blank=True))])), ('side_note', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('linked_image', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock(blank=True)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True),
        ),
        migrations.AlterField(
            model_name='articlesectiones',
            name='section_addons',
            field=wagtail.core.fields.StreamField([('effects', wagtail.core.blocks.StructBlock([('positive_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('neutral_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock())), ('negative_effects', wagtail.core.blocks.ListBlock(wagtail.core.blocks.CharBlock()))])), ('content', wagtail.core.blocks.RichTextBlock(blank=True)), ('table_of_three', wagtail.core.blocks.StructBlock([('title_1', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_1', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_2', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_2', wagtail.core.blocks.RichTextBlock(blank=True)), ('title_3', wagtail.core.blocks.CharBlock(blank=True, max_length=10)), ('content_3', wagtail.core.blocks.RichTextBlock(blank=True))])), ('interactions', wagtail.core.blocks.StructBlock([('interactions', wagtail.core.blocks.ListBlock(article.models.Interaction))])), ('brain_tip', wagtail.core.blocks.StructBlock([('click_the_brain_text', wagtail.core.blocks.CharBlock(blank=True, default='Click the brain for neuro-info!', max_length=255)), ('content', wagtail.core.blocks.RichTextBlock(blank=True))])), ('side_note', wagtail.core.blocks.StructBlock([('content', wagtail.core.blocks.RichTextBlock())])), ('linked_image', wagtail.core.blocks.StructBlock([('name', wagtail.core.blocks.CharBlock()), ('link', wagtail.core.blocks.URLBlock(blank=True)), ('image', wagtail.images.blocks.ImageChooserBlock())]))], blank=True),
        ),
    ]
