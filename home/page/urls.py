from django.urls import path
from page.views import home_page

urlpatterns = [
    path("", home_page, name="home_page"),
]
