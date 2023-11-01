from django.contrib import admin

# Register your models here.
from .models import Advertisement

# Register your models here.
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','address', 'phone',)
    list_display_links = ('id','title',)
    search_fields = ('title',)


admin.site.register(Advertisement,AdvertisementAdmin)
