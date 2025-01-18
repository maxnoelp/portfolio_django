from django.shortcuts import render
from django.views.generic import DetailView
from portfolio.landingpage.models import AboutMeText


class AboutMeView(DetailView):
    model = AboutMeText
    template_name = "landingpage/landingpage.html"
    context_object_name = "about"
