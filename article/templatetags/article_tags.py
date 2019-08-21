from django import template
from article.models import (Highlight, SocialMedia, FooterLink, ArticlePage,
                            ArticleConstants, Page)
from blog.models import BlogIndexPage
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

@register.simple_tag
def blog_activated():
    blogs = BlogIndexPage.objects.all()
    blog = [x for x in blogs if x.title == "Blog"][0]
    if is_live_or_not(blog):
        return blog


def filtered_articles(category=None):
    articles = list(ArticlePage.objects
                    .order_by('title_' + get_language()[:2])
                    .live())
    if category:
        articles = filter(lambda x: x.categories.first().name == category,
                          articles)
    return list(articles)

def is_live_or_not(page):
    if page.specific_class == ArticlePage:
        return page.live and page.specific.is_published
    if page.specific_class == BlogIndexPage:
        return page.live and page.specific.is_published
    else:
        return page.live


def pages_in_folder(folder_name):
    pages = list(Page.objects.order_by('title'))
    folder = list(filter(lambda x: x.title == folder_name, pages))[0]
    pages_in_folder = filter(lambda x: x.is_child_of(folder),  pages)
    live_pages_in_folder = filter(lambda x: is_live_or_not(x), list(pages_in_folder))
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

@register.filter
def length(arr):
    return len(arr)
