from django.contrib import admin
from smileys.models import Smiley
from django.utils.translation import ugettext_lazy as _
from easy_thumbnails.files import get_thumbnailer

class SmileyAdmin(admin.ModelAdmin):
    list_select_related = True
    list_display = ['id', 'pattern', 'description', 'get_icon_link', 'image', 'is_regex', 'is_active', 'tags']
    list_filter = ['is_active', 'is_regex']
    list_editable = ['tags']
    readonly_fields = []
    search_fields = ['description', 'tags']
    #---------------------------------- Récupérer un markup de l'image avec lien
    def get_icon_link(self, obj):
        if obj.image:
            thumbnailer = get_thumbnailer(obj.image.name)
            thumbnail_options = {'crop': True, 'size':(32,32)}
            result = thumbnailer.get_thumbnail(thumbnail_options)
            return "<img src='%s'>" % (obj.image.url)
        else:
            return u"<em>%s</em>" % _(u"None")
    get_icon_link.allow_tags = True
    get_icon_link.short_description = _(u"Image")

admin.site.register(Smiley, SmileyAdmin)
