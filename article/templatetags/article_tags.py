from django import template
from article.models import (Highlight, SocialMedia, FooterLink, ArticlePage,
                            ArticleConstants, Page)
from django.utils.translation import get_language

register = template.Library()


@register.simple_tag
def cookie_banner():
    constants = article_constants()

    class CookieBanner:
        message = None
        button = None
        link = None

    cookie_banner = CookieBanner()
    cookie_banner.message = constants.cookie_banner_message
    cookie_banner.button = constants.cookie_banner_button
    cookie_banner.link = constants.cookie_banner_link
    return cookie_banner


@register.simple_tag
def highlights():
    return Highlight.objects.all()


@register.simple_tag
def social_media():
    return SocialMedia.objects.all()


@register.simple_tag
def footer_links():
    links = list(list(FooterLink.objects
                      .order_by('name_' + get_language()[:2])))
    return links


@register.simple_tag
def all_pages():
    return filtered_articles()


def filtered_articles(category=None):
    articles = list(ArticlePage.objects
                    .order_by('title_' + get_language()[:2])
                    .live())
    if category:
        articles = filter(lambda x: x.categories.first().name == category,
                          articles)
    return list(articles)


def pages_in_folder(folder_name):
    pages = list(Page.objects.order_by('title'))
    folder = list(filter(lambda x: x.title == folder_name, pages))[0]
    pages_in_folder = filter(lambda x: x.is_child_of(folder),  pages)
    live_pages_in_folder = filter(lambda x: x.live, list(pages_in_folder))
    return list(live_pages_in_folder)


@register.simple_tag
def drug_pages():
    return pages_in_folder("Drugs")


@register.simple_tag
def info_pages():
    return pages_in_folder("Info")


@register.simple_tag
def me_pages():
    return pages_in_folder("Me")


@register.simple_tag
def article_constants():
    return ArticleConstants.objects.first()


@register.filter
def pdb(element):
    import pdb
    pdb.set_trace()
    return element


@register.filter
def dir(thing):
    return thing.__dir__()
