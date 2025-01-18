from portfolio.landingpage.views import AboutMeView
from django.urls import path

app_name = "portfolio.landingpage"
urlpatterns = [
    path("", AboutMeView.as_view(), name="aboutMe"),
]
