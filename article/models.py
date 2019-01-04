from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.blocks import (StructBlock, ListBlock, CharBlock,
                                 RichTextBlock)
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel, StreamFieldPanel)
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from colorfield.fields import ColorField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from django import forms
from django.utils import translation
from wagtail.admin.edit_handlers import TabbedInterface, ObjectList
from code_snippets.models import CodeSnippetBlock


class TranslatedField:
    en_field = ""
    es_field = ""

    def init(self, field_type, var_names, **kwargs):
        self.en_field = var_names[0]
        self.es_field = var_names[1]
        if field_type is not None:
            lang_en = field_type(**kwargs)
            lang_es = field_type(**kwargs)
            return lang_en, lang_es

    def __get__(self, instance, owner):
        if translation.get_language() == 'es':
            return getattr(instance, self.es_field)
        else:
            return getattr(instance, self.en_field)


@register_snippet
class ArticleConstants(models.Model):
    select_a_drug = TranslatedField()
    select_a_drug_en, select_a_drug_es = select_a_drug.init(
        models.CharField,
        ('select_a_drug_en', 'select_a_drug_es'),
        max_length=30, blank=True)

    no_drug_selected_text = TranslatedField()
    no_drug_selected_text_en, no_drug_selected_text_es = no_drug_selected_text.init(
        models.CharField,
        ('no_drug_selected_text_en', 'no_drug_selected_text_es'),
        max_length=255, blank=True)

    source = TranslatedField()
    source_en, source_es = source.init(
        models.CharField,
        ('source_en', 'source_es'),
        max_length=15, blank=True)

    campaign_caption = TranslatedField()
    campaign_caption_en, campaign_caption_es = campaign_caption.init(
        RichTextField,
        ('campaign_caption_en', 'campaign_caption_es'),
        blank=True)

    cookie_banner_message = TranslatedField()
    cookie_banner_message_en, cookie_banner_message_es = cookie_banner_message.init(
        models.TextField,
        ('cookie_banner_message_en', 'cookie_banner_message_es'),
        blank=True)

    cookie_banner_button = TranslatedField()
    cookie_banner_button_en, cookie_banner_button_es = cookie_banner_button.init(
        models.TextField,
        ('cookie_banner_button_en', 'cookie_banner_button_es'),
        blank=True)

    cookie_banner_link = TranslatedField()
    cookie_banner_link_en, cookie_banner_link_es = cookie_banner_link.init(
        models.URLField,
        ('cookie_banner_link_en', 'cookie_banner_link_es'),
        blank=True)

    default_share_blurb = TranslatedField()
    default_share_blurb_en, default_share_blurb_es = default_share_blurb.init(
        models.TextField,
        ('default_share_blurb_en', 'default_share_blurb_es'),
        blank=True)

    panels = [
        FieldPanel('select_a_drug_en'),
        FieldPanel('no_drug_selected_text_en'),
        FieldPanel('source_en'),
        FieldPanel('campaign_caption_en'),
        FieldPanel('cookie_banner_message_en'),
        FieldPanel('cookie_banner_button_en'),
        FieldPanel('cookie_banner_link_en')



    ]
    panels_es = [
        FieldPanel('select_a_drug_es'),
        FieldPanel('no_drug_selected_text_es'),
        FieldPanel('source_es'),
        FieldPanel('campaign_caption_es'),
        FieldPanel('cookie_banner_message_es'),
        FieldPanel('cookie_banner_button_es'),
        FieldPanel('cookie_banner_link_es')



    ]
    edit_handler = TabbedInterface([
        ObjectList(panels, heading='EN Content'),
        ObjectList(panels_es, heading='ES content'),
    ])

    def __str__(self):
        return "Article constants"


@register_snippet
class ArticleCategory(models.Model):

    name = TranslatedField()
    name_en, name_es = name.init(
        models.CharField,
        ('name_en', 'name_es'),
        max_length=255, blank=True)

    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name_en'),
        ImageChooserPanel('icon'),
    ]

    panels_es = [
        FieldPanel('name_es'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='EN Content'),
        ObjectList(panels_es, heading='ES content'),
    ])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'article categories'


@register_snippet
class SocialMedia(models.Model):
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
        FieldPanel('link'),
        FieldPanel('icon')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Social media links'


@register_snippet
class Highlight(models.Model):

    name = TranslatedField()
    name_en, name_es = name.init(
        models.CharField,
        ('name_en', 'name_es'),
        max_length=50, blank=True, default="")

    link = TranslatedField()
    link_en, link_es = link.init(
        models.CharField,
        ('link_en', 'link_es'),
        max_length=255, default='')

    def __str__(self):
        return self.name

    colour = ColorField(default='#FFF')

    panels = [
        FieldPanel('name_en'),
        FieldPanel('link_en'),
        FieldPanel('colour'),
    ]
    panels_es = [
        FieldPanel('name_es'),
        FieldPanel('link_es'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='EN Content'),
        ObjectList(panels_es, heading='ES content'),
    ])

    class Meta:
        verbose_name_plural = 'Highlights'


@register_snippet
class FooterLink(models.Model):
    name = TranslatedField()
    name_en, name_es = name.init(
        models.CharField,
        ('name_en', 'name_es'),
        max_length=50, blank=True, default="")

    link = TranslatedField()
    link_en, link_es = link.init(
        models.CharField,
        ('link_en', 'link_es'),
        max_length=255, default='')

    panels = [
        FieldPanel('name_en'),
        FieldPanel('link_en'),
    ]

    panels_es = [
        FieldPanel('name_es'),
        FieldPanel('link_es'),
    ]

    edit_handler = TabbedInterface([
        ObjectList(panels, heading='EN Content'),
        ObjectList(panels_es, heading='ES content'),
    ])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Footer links'


@register_snippet
class InteractionType(models.Model):

    name = TranslatedField()
    name_en, name_es = name.init(
        models.CharField,
        ('name_en', 'name_es'),
        max_length=50, blank=True, default="")

    default_description = TranslatedField()
    default_description_en, default_description_es = default_description.init(
        RichTextField,
        ('default_description_en', 'default_description_es'),
        max_length=300, blank=True)

    colour = ColorField(default='#6c6c6c')

    panels = [
        FieldPanel('name_en'),
        FieldPanel('default_description_en'),
        FieldPanel('colour')
    ]

    panels_es = [
        FieldPanel('name_es'),
        FieldPanel('default_description_es')
    ]

    edit_handler = TabbedInterface([
            ObjectList(panels, heading='EN Content'),
            ObjectList(panels_es, heading='ES content'),
        ])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'interaction types'


class Interaction(StructBlock):
    drug_name = CharBlock(max_length=13, blank=True)
    interaction_type = SnippetChooserBlock("article.InteractionType")
    description = RichTextBlock(required=False)

    class Meta:
        abstract = True


class Interactions(StructBlock):
    interactions = ListBlock(Interaction)

    class Meta:
        template = "article/interactions.html"


class EffectsBlock(StructBlock):
    # var names "positive_effects", "neutral_effects", "negative_effects"
    # cannot be used as they reference older variables in the StreamField
    # This is messy, but I can't figure out how to fix it.
    positive_effects_new = RichTextBlock(blank=True)
    neutral_effects_new = RichTextBlock(blank=True)
    negative_effects_new = RichTextBlock(blank=True)

    class Meta:
        template = "article/effects.html"


class TableOfThree(StructBlock):
    title_1 = CharBlock(max_length=10, blank=True)
    content_1 = RichTextBlock(blank=True)
    title_2 = CharBlock(max_length=10, blank=True)
    content_2 = RichTextBlock(blank=True)
    title_3 = CharBlock(max_length=10, blank=True)
    content_3 = RichTextBlock(blank=True)

    class Meta:
        template = "article/table.html"


class BrainTip(StructBlock):
    click_the_brain_text = CharBlock(max_length=255,
                                     blank=True,
                                     default="Click the brain for neuro-info!")
    content = RichTextBlock(blank=True)

    class Meta:
        template = "article/brain-tip.html"


class SideNote(StructBlock):
    content = RichTextBlock()

    class Meta:
        template = "article/side-note.html"


class Section (models.Model):
    section_name = models.CharField(max_length=50, blank=True)
    section_content = RichTextField(blank=True)

    section_addons = StreamField([
        ('effects', EffectsBlock()),
        ('content', RichTextBlock(blank=True)),
        ('table_of_three', TableOfThree()),
        ('interactions', Interactions()),
        ('brain_tip', BrainTip()),
        ('side_note', SideNote()),
        ('code', CodeSnippetBlock("code_snippets.CodeSnippet"))
        # ('effects', EffectsBlock(icon="fa-stethoscope")),
        # ('content', RichTextBlock(blank=True, icon="fa-paragraph")),
        # ('table_of_three', TableOfThree(icon="fa-the-list")),
        # ('interactions', ListBlock(Interaction(), icon="fa-flask")),
        ], blank=True)
    panels = [
        FieldPanel('section_name'),
        FieldPanel('section_content'),
        StreamFieldPanel('section_addons')
    ]

    @property
    def section_id(self):
        return self.section_name.replace(" ", "-")

    class Meta:
        abstract = True


class ArticleSectionEN(Orderable, Section):
    article = ParentalKey(
        'ArticlePage',
        related_name='sections_en',
        on_delete=models.CASCADE
    )


class ArticleSectionES(Orderable, Section):
    article = ParentalKey(
        'ArticlePage',
        related_name='sections_es',
        on_delete=models.CASCADE
    )


class ThingToTake(models.Model):

    front_text = models.CharField(max_length=20, blank=True)
    back_text = models.CharField(max_length=175, blank=True)
    panels = [
        FieldPanel('front_text'),
        FieldPanel('back_text'),
    ]

    class Meta:
        abstract = True


class ArticleTipsEN(Orderable, ThingToTake):

    tips = ParentalKey(
        'ArticlePage',
        related_name='things_to_take_en',
        on_delete=models.CASCADE
    )


class ArticleTipsES(Orderable, ThingToTake):

    tips = ParentalKey(
        'ArticlePage',
        related_name='things_to_take_es',
        on_delete=models.CASCADE
    )


class ArticlePage(Page):

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

    blurb = TranslatedField()
    blurb_en, blurb_es = blurb.init(
        RichTextField,
        ('blurb_en', 'blurb_es'),
        blank=True)

    intro = TranslatedField()
    intro_en, intro_es = intro.init(
        RichTextField,
        ('intro_en', 'intro_es'),
        blank=True)

    colour = ColorField(default='#6c6c1c')
    categories = ParentalManyToManyField('article.ArticleCategory')
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

    intro_extras = StreamField([
        ('code_snippet', CodeSnippetBlock("code_snippets.CodeSnippet"))
    ], blank=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("seo_title_en"),
            FieldPanel("seo_description_en"),
            FieldPanel("blurb_en"),
        ], heading="Promote"),
        MultiFieldPanel([
            FieldPanel('title_en'),
            FieldPanel('sub_title_en'),
            FieldPanel('colour'),
            ImageChooserPanel('cover_image'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Cover"),
        FieldPanel('intro_en'),
        InlinePanel('things_to_take_en', label="Things to take"),
        StreamFieldPanel('intro_extras'),
        InlinePanel('sections_en', label="Section")
    ]

    es_content_panels = [
        MultiFieldPanel([
            FieldPanel("seo_title_es"),
            FieldPanel("seo_description_es"),
            FieldPanel("blurb_es"),
        ], heading="Promote"),
        FieldPanel('title_es'),
        FieldPanel('sub_title_es'),
        FieldPanel('intro_es'),
        InlinePanel('things_to_take_es'),
        InlinePanel('sections_es', label="Sección"),
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

    sections = TranslatedField()
    sections.init(None, ('sections_en', 'sections_es'))

    things_to_take = TranslatedField()
    things_to_take.init(None, ('things_to_take_en', 'things_to_take_es'))

    @property
    def related_names(self):
        return self.sub_title.split(", ")

    @property
    def things_to_take_en(self):
        tips = self.things_to_take_en.all()
        return tips

    @property
    def sections_en(self):
        article = self.sections_en.all()
        return article

    @property
    def things_to_take_es(self):
        tips = self.things_to_take_es.all()
        return tips

    @property
    def sections_es(self):
        article = self.sections_es.all()
        return article
