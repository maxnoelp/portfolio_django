from django.views.generic import TemplateView

from portfolio.landingpage.filters import ProjectTagsFilter
from portfolio.landingpage.models import AboutMeText
from portfolio.landingpage.models import CodeProjects
from portfolio.landingpage.models import CodingSkills


class LandingPageView(TemplateView):
    template_name = "landingpage/landingpage.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["about"] = AboutMeText.objects.all()
        context["skills"] = CodingSkills.objects.all()
        context["projects"] = CodeProjects.objects.all()
        tags = ProjectTagsFilter(self.request.GET, queryset=CodeProjects.objects.all())

        context["filter"] = tags
        context["projects"] = tags.qs
        return context
