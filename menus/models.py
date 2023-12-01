from django.db import models
# Create your models here.

from wagtail.snippets.models import register_snippet


from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.models import Orderable
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel



class PageList(Orderable):
    nav_item = ParentalKey('NavItem', related_name='page_lists')
    link = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    panels = [
        PageChooserPanel('link')
    ]

class NavItem(ClusterableModel, Orderable):
    title = models.CharField(max_length=20, blank=True, null=True)
    navbar = ParentalKey('Navbar', related_name='nav_items')
    panels = [
        FieldPanel('title'),
        InlinePanel('page_lists', label='Dropdown')
    ]

    @property
    def nav_tab_title(self):
        if self.title:
            return self.title
        else:
            return self.page_lists.all()[0].link.title
        
    @property
    def nav_tab_link(self):
        if not self.title:
            return self.page_lists.all()[0].link.url



@register_snippet
class Navbar(ClusterableModel):
    panels = [
        InlinePanel('nav_items', label='Add Nav Item')
    ]

    def __str__(self):
        return "Navbar"