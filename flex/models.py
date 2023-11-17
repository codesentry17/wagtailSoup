from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail import blocks
from wagtail.images.blocks import ImageChooserBlock
from wagtail.fields import RichTextField, StreamField

# Create your models here.

class FlexPage(Page):

    banner_subtitle = models.CharField(max_length=100, blank=True, null=True)

    body = RichTextField(blank=False, null=True)

    """superNova = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)"""

    content_panels = Page.content_panels + [
        FieldPanel('banner_subtitle'),
        FieldPanel('body')
    ]


#checking streamfields...
class pageify(Page):
    author = models.CharField(max_length=255)
    date = models.DateField("Post date")
    body = StreamField([
        ('heading', blocks.CharBlock(form_classname="title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('author'),
        FieldPanel('date'),
        FieldPanel('body'),
    ]

    

