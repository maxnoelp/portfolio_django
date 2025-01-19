from django.urls import path

from portfolio.landingpage.views import LandingPageView

app_name = "portfolio.landingpage"
urlpatterns = [
    path("", LandingPageView.as_view(), name="aboutMe"),
]
