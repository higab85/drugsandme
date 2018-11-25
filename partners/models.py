from django.db import models
from article.models import TranslatedField
from wagtail.core.models import Page
from colorfield.fields import ColorField
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from django import forms
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from wagtail.search import index


# Create your models here.
class PartnersPage(Page):

        translated_title = TranslatedField()
        title_en, title_es = translated_title.init(
            models.CharField,
            ('title_en', 'title_es'),
            max_length=255, blank=True)

        def get_title():
            return str(translated_title)

        sub_title = TranslatedField()
        sub_title_en, sub_title_es = sub_title.init(
            models.CharField,
            ('sub_title_en', 'sub_title_es'),
            max_length=255, blank=True)

        intro = TranslatedField()
        intro_en, intro_es = intro.init(
            RichTextField,
            ('intro_en', 'intro_es'),
            blank=True)

        colour = ColorField(default='#6c6c1c')
        cover_image = models.ForeignKey(
            'wagtailimages.Image',
            null=True,
            # blank=True,
            on_delete=models.SET_NULL,
            related_name='+'
        )

        translated_seo_title = TranslatedField()
        seo_title_en, seo_title_es = translated_seo_title.init(
            models.TextField,
            ('seo_title_en', 'seo_title_es'),
            blank=True)
        translated_seo_description = TranslatedField()
        seo_description_en, seo_description_es = translated_seo_description.init(
            models.TextField,
            ('seo_description_en', 'seo_description_es'),
            blank=True)

        content_panels = Page.content_panels + [
            MultiFieldPanel([
                FieldPanel("seo_title_en"),
                FieldPanel("seo_description_en"),
            ], heading="Promote"),
            MultiFieldPanel([
                FieldPanel('title_en'),
                FieldPanel('sub_title_en'),
                FieldPanel('colour'),
                ImageChooserPanel('cover_image'),
            ], heading="Cover"),
            FieldPanel('intro_en'),
        ]

        es_content_panels = [
            MultiFieldPanel([
                FieldPanel("seo_title_es"),
                FieldPanel("seo_description_es"),
            ], heading="Promote"),
            FieldPanel('title_es'),
            FieldPanel('sub_title_es'),
            FieldPanel('intro_es'),
        ]

        edit_handler = TabbedInterface([
            ObjectList(content_panels, heading='EN Content'),
            ObjectList(es_content_panels, heading='ES content'),
            ObjectList(Page.promote_panels, heading='Promote'),
            ObjectList(Page.settings_panels, heading='Settings',
                       classname="settings"),
        ])

        search_fields = Page.search_fields + [
            index.SearchField('title_en'),
            index.SearchField('title_es'),
            index.SearchField('sub_title_en'),
            index.SearchField('sub_title_es'),

        ]

        def __str__(self):
            return self.title
