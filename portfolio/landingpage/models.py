from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from filer.fields.image import FilerImageField

from portfolio.landingpage.utils import CODE_LANGUAGE


class AboutMeText(models.Model):
    text = RichTextField(_("Über mich"))
    image = FilerImageField(
        verbose_name=_("Bild"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    image_alt = models.CharField(_("Image Alt Text"), max_length=200)
    image_title = models.CharField(_("Image Titel"), max_length=200)

    def __str__(self):
        return self.image_title


class CodingSkills(models.Model):
    icon = FilerImageField(
        verbose_name=_("Icon"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    description = models.CharField(_("Code Language"), blank=True, max_length=100)

    def __str__(self):
        return self.description


class CodeProjects(models.Model):
    title = models.CharField(_("Titel"), max_length=100)
    tag = models.CharField(_("Wähle ein Tag aus"), choices=CODE_LANGUAGE, default="")
    text = RichTextField(_("Beschreibung"))
    image_left = FilerImageField(
        verbose_name=_("linkes Bild"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="codeproject_left_images",
    )
    image_left_alt = models.CharField(_("links Image Alt Text"), max_length=200)
    image_left_title = models.CharField(_("links Image Titel"), max_length=200)
    image_right = FilerImageField(
        verbose_name=_("rechtes Bild"),
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name="codeproject_right_images",
    )
    image_right_alt = models.CharField(_("Image rechts Alt Text"), max_length=200)
    image_right_title = models.CharField(_("Image rechts Titel"), max_length=200)
    # url repository
    # url title

    def __str__(self):
        return self.title
