from wagtail.core.fields import RichTextField
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.core.models import Page, Orderable
from wagtail.admin.edit_handlers import (FieldPanel, InlinePanel,
                                         MultiFieldPanel)
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.search import index
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.snippets.models import register_snippet
from django import forms
from article.models import TranslatedField
from colorfield.fields import ColorField
from django.utils import translation
from operator import attrgetter


# Retreive snippets: blog.models.BlogCategory.objects.all()

class Mention(Page):

    organisation_name = models.TextField()
    publication_date = models.DateField()
    author = RichTextField()
    article_link = models.URLField()
    summary = RichTextField()

    organisation_logo = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('summary'),
        index.SearchField('organisation_name'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('organisation_name'),
        FieldPanel('publication_date'),
        FieldPanel('author'),
        FieldPanel('article_link'),
        ImageChooserPanel('organisation_logo'),
        FieldPanel('summary'),
    ]

    def get_sitemap_urls(self, request=None):
        return []


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


@register_snippet
class BlogPageLanguage(models.Model):

    name = models.CharField(max_length=255, blank=True)
    lang_code = models.CharField(max_length=2, blank=True)

    panels = [
        FieldPanel('name'),
        FieldPanel('lang_code')
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog languages'


class BlogPage(Page):
    sub_title = models.CharField(max_length=255, blank=True)
    publication_date = models.DateField("Post date")
    colour = ColorField(default='#bbcee5')
    language = ParentalManyToManyField('blog.BlogPageLanguage')
    intro = RichTextField(blank=True)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        # blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('sub_title'),
            FieldPanel('publication_date'),
            ImageChooserPanel('cover_image'),
            FieldPanel('language'),
            FieldPanel('colour'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage,
                       on_delete=models.CASCADE,
                       related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogIndexPage(Page):
    cover_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        # blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    colour = ColorField(default='#bbcee5')
    translated_title = TranslatedField()
    title_en, title_es = translated_title.init(
        models.CharField,
        ('title_en', 'title_es'),
        max_length=255, blank=True)

    sub_title = TranslatedField()
    sub_title_en, sub_title_es = sub_title.init(
        models.CharField,
        ('sub_title_en', 'sub_title_es'),
        max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('title_en'),
        FieldPanel('title_es'),
        FieldPanel('sub_title_en'),
        FieldPanel('sub_title_es'),
        ImageChooserPanel('cover_image'),
        FieldPanel('colour'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by
        # reverse-chron
        context = super().get_context(request)
        entries = self.get_children().live()
        specific_entries = list(map(lambda x: x.specific, entries))
        if type(specific_entries[0]) == BlogPage:
            specific_entries = filter(
                lambda x: x.language.first().lang_code ==
                translation.get_language()[:2], specific_entries)
            context['class_type'] = 'blogpage'
        else:
            context['class_type'] = 'mention'
        sorted_entries = sorted(specific_entries,
                                key=attrgetter("publication_date"),
                                reverse=True)
        context['entries'] = sorted_entries
        return context
