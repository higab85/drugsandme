from django.db import models
from wagtail.images.models import Image, AbstractImage, AbstractRendition


class CustomImage(AbstractImage):

    link = models.URLField(blank=True)
    description = models.TextField(blank=True)

    admin_form_fields = Image.admin_form_fields + (
        'link',
        'description',
    )


class CustomRendition(AbstractRendition):
    image = models.ForeignKey(CustomImage,
                              on_delete=models.CASCADE,
                              related_name='renditions')

    class Meta:
        unique_together = (
            ('image', 'filter_spec', 'focal_point_key'),
        )
