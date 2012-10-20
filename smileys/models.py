from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
import os

class SmileyManager(models.Manager):
    def active(self):
        return self.get_query_set().filter(is_active=True)

class Smiley(models.Model):
    pattern = models.CharField(max_length=24, verbose_name=_("Pattern"))
    description = models.CharField(max_length=128, blank=True, verbose_name=_("Description"))
    image = models.ImageField(upload_to=getattr(settings, 'SMILEYS_PATH', 'smileys'), verbose_name=_("Image"))
    is_regex = models.BooleanField(blank=True, verbose_name=_("Is a regex"))
    is_active = models.BooleanField(default=True, blank=True, verbose_name=_("Active"))
    tags = models.CharField(max_length=64, blank=True, verbose_name=_("Tags"))

    def save(self, *args, **kwargs):
        if self.image:
            try:
                os.remove(self.image.name)
            except:
                pass
        super(Smiley, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        try:
            os.remove(self.image.name)
        except:
            pass
        super(Smiley, self).delete(*args, **kwargs)

    def __unicode__(self):
        return self.description or self.pattern

    class Meta:
        ordering = ('description', 'pattern')
        verbose_name = _(u"Smiley")
        verbose_name_plural = _(u"Smileys")
