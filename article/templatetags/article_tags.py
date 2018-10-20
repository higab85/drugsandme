from django import template
from article.models import Highlight, SocialMedia, FooterLink, ArticlePage, ArticleConstants
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag
def highlights():
    return Highlight.objects.all()

@register.simple_tag
def social_media():
    return SocialMedia.objects.all()

@register.simple_tag
def footer_links():
    links = list(list(FooterLink.objects.order_by('name_' + get_language()[:2])))
    return links

@register.simple_tag
def all_pages():
    return filtered_articles()

def filtered_articles(category=None):
    articles = list(ArticlePage.objects.order_by('title_' + get_language()[:2]).live())
    if category:
        articles = filter(lambda x: x.categories.first().name == category,  articles)
    return list(articles)


@register.simple_tag
def drug_pages():
    return filtered_articles(category="Drug")

@register.simple_tag
def info_pages():
    return filtered_articles(category="Info")

@register.simple_tag
def me_pages():
    return filtered_articles(category="Me")

@register.simple_tag
def article_constants():
    return ArticleConstants.objects.first()
