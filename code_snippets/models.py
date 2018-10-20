from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import RawHTMLBlock
from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel


@register_snippet
class CodeSnippet(models.Model):
    title = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    code_samples = StreamField([
        ('code', RawHTMLBlock())
    ], blank=True)


    panels = [
        FieldPanel('title'),
        FieldPanel('description'),
        StreamFieldPanel('code_samples')
    ]

    def __str__(self):
        return self.title

class CodeSnippetBlock(SnippetChooserBlock):
    class Meta:
        template = "code_snippets/code_snippet.html"
