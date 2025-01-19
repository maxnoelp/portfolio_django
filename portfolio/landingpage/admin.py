from django.contrib import admin

from portfolio.landingpage.models import AboutMeText
from portfolio.landingpage.models import CodeProjects
from portfolio.landingpage.models import CodingSkills


@admin.register(AboutMeText)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ("text", "image")


@admin.register(CodeProjects)
class CodeProjectsAdmin(admin.ModelAdmin):
    actions = ["duplicate_objects"]

    @admin.action(
        description="Ausgewählte Objekte duplizieren",
    )
    def duplicate_objects(self, request, queryset):
        for obj in queryset:
            obj.pk = None
            obj.save()
        self.message_user(request, "Ausgewählte Objekte wurden erfolgreich dupliziert.")


admin.site.register(CodingSkills)
