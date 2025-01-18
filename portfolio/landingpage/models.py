from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField


class AboutMeText(models.Model):
    text = RichTextField(_("Über mich"))
    image = FilerImageField(_("Bild"))
    image_alt = models.CharField(_("Image Alt Text"), max_length=200)
    image_title = models.CharField(_("Image Titel"), max_length=200)

    def __str__(self):
        return self.image_title
