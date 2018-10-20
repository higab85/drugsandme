from django import template
from blog.models import BlogPage
from django.utils.translation import get_language

register = template.Library()

@register.simple_tag
def blog_posts(self):
    live_blog_posts = list(BlogPage.objects.live())
    blog_posts = filter(lambda x: x.language.first().lang_code == get_language()[:2],  live_blog_posts)
    return list(blog_posts)



# @register.simple_tag
# def article_constants():
#     return ArticleConstants.objects.first()
