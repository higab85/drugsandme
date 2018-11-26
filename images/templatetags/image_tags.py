from django import template
from images.models import CustomImage

register = template.Library()


@register.simple_tag
def partners():
    partners = []
    for image in all_images():
        if "partner" in image.tags.names():
            partners.append(image)
    return partners

@register.simple_tag
def all_images():
    images = list(CustomImage.objects.all())
    return images
