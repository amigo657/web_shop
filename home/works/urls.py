from django.urls import path
from works.views import our_works

urlpatterns = [
    path("", our_works, name="our_works")
]