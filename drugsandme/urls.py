from django.conf import settings
from django.conf.urls import include, url
from django.urls import path
from django.contrib import admin
from django.conf.urls.i18n import i18n_patterns

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views
from drugsandme import views

from wagtail.contrib.sitemaps.views import sitemap

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),

    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),

    url(r'^search/$', search_views.search, name='search'),


    url('^sitemap\.xml$', sitemap),
    # path('<slug>.html', views.drugs),

    path('cannabis', views.cannabis),
    path('en/cannabis', views.cannabis),

    path('cocaine', views.cocaine),
    path('en/cocaine', views.cocaine),

    path('ketamine', views.ketamine),
    path('en/ketamine', views.ketamine),

    path('lsd', views.lsd),
    path('en/lsd', views.lsd),

    path('mdma', views.mdma),
    path('en/mdma', views.mdma),

    path('modafinil', views.modafinil),
    path('en/modafinil', views.modafinil),



    # # For anything not caught by a more specific rule above, hand over to
    # # Wagtail's page serving mechanism. This should be the last pattern in
    # # the list:
    # url(r'', include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r'^pages/', include(wagtail_urls)),
]


urlpatterns += i18n_patterns(
    # These URLs will have /<language_code>/ appended to the beginning

    url(r'^search/$', search_views.search, name='search'),

    url(r'', include(wagtail_urls)),
)


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
