from portfolio.landingpage.views import AboutMeView
from django.urls import path

app_name = "portfolio.landingpage"
urlpatterns = [
    path("", view=AboutMeView, name="aboutMe"),
]
