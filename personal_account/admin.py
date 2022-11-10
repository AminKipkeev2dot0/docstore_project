from django.contrib import admin


# Register your models here.
from .models import Doc
class DocAdmin(admin.ModelAdmin):
    list_display=('title','descr','scan')
    # list_display_links=('title','descr')
    search_fields=('title','descr')

admin.site.register(Doc,DocAdmin)


     