from django.contrib import admin

from portfolio.landingpage.models import AboutMeText


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("text", "image")


admin.site.register(AboutMeText, AboutMeAdmin)
