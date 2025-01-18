from django.shortcuts import render
from django.views.generic import ListView
from portfolio.landingpage.models import AboutMeText


class AboutMeView(ListView):
    model = AboutMeText
    template_name = "landingpage/landingpage.html"
    context_object_name = "about"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context["about"])
        return context
