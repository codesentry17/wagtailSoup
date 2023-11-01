from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel, PageChooserPanel
from wagtail.fields import RichTextField


class HomePage(Page):
    
    max_count = 1

    banner_title = models.CharField(max_length=100, blank=False, null=True)

    banner_subtitle = RichTextField(blank=False, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_subtitle')
    ]