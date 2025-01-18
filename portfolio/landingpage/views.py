from django.views.generic import ListView

from portfolio.landingpage.models import AboutMeText
from portfolio.landingpage.models import CodeProjects
from portfolio.landingpage.models import CodingSkills


class AboutMeView(ListView):
    model = AboutMeText
    template_name = "landingpage/landingpage.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CodingSkillView(ListView):
    model = CodingSkills
    template_name = "landingpage/landingpage.html"
    context_object_name = "skill"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class CodeProjects(ListView):
    model = CodeProjects
    template_name = "landingpage/landingpage.html"
    context_object_name = "code"

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
