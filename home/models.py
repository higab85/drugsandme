from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import StreamField
from wagtail.core.blocks import (StructBlock, ListBlock, CharBlock,
                                 RichTextBlock)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.admin.edit_handlers import (FieldPanel, StreamFieldPanel,
                                         InlinePanel, TabbedInterface,
                                         ObjectList)
from modelcluster.fields import ParentalKey
from article.models import TranslatedField
from django.utils import translation



class Partner(StructBlock):
    name = CharBlock(max_length=25, blank=True)
    link = CharBlock(max_length=255, blank=True)
    logo = ImageChooserBlock()

    class Meta:
        template = "home/partner.html"
        abstract = True


class IndexSection (models.Model):
    section_name = models.CharField(max_length=50, blank=True)

    section_content = StreamField([
        ('text', RichTextBlock()),
        ('partners', ListBlock(Partner())),
        ], blank=True)

    panels = [
        FieldPanel('section_name'),
        StreamFieldPanel('section_content')
    ]

    @property
    def section_id(self):
        return self.section_name.replace(" ", "-")

    class Meta:
        abstract = True


class IndexBlurbEN(Orderable, IndexSection):
    article = ParentalKey(
        'HomePage',
        related_name='index_sections_en',
        on_delete=models.CASCADE
    )


class IndexBlurbES(Orderable, IndexSection):
    article = ParentalKey(
        'HomePage',
        related_name='index_sections_es',
        on_delete=models.CASCADE
    )


class HomePage(Page):

    def serve(self, request):
        translation.activate("en")
        # request.LANGUAGE_CODE = "en"
        return super().serve(request)

    title_tip_drugs = TranslatedField()
    title_tip_drugs_en, title_tip_drugs_es = title_tip_drugs.init(
        models.CharField,
        ('title_tip_drugs_en', 'title_tip_drugs_es'),
        max_length=255, blank=True)

    title_tip_me = TranslatedField()
    title_tip_me_en, title_tip_me_es = title_tip_me.init(
        models.CharField,
        ('title_tip_me_en', 'title_tip_me_es'),
        max_length=255, blank=True)

    title_lead = TranslatedField()
    title_lead_en, title_lead_es = title_lead.init(
        models.CharField,
        ('title_lead_en', 'title_lead_es'),
        max_length=255, blank=True)

    panels = Page.content_panels + [
        FieldPanel('title_tip_drugs_en'),
        FieldPanel('title_tip_me_en'),
        FieldPanel('title_lead_en'),
        InlinePanel('index_sections_en', label="Section"),
    ]
    panels_es = [
        FieldPanel('title_tip_drugs_es'),
        FieldPanel('title_tip_me_es'),
        FieldPanel('title_lead_es'),
        InlinePanel('index_sections_es', label="Section"),
    ]
    edit_handler = TabbedInterface([
        ObjectList(panels, heading='EN Content'),
        ObjectList(panels_es, heading='ES content'),
    ])

    index_sections = TranslatedField()
    index_sections.init(None, ('index_sections_en', 'index_sections_es'))

    @property
    def index_sections_en(self):
        article = self.index_sections_en.all()
        return article

    @property
    def index_sections_es(self):
        article = self.index_sections_es.all()
        return article
