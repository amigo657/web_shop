from django.urls import path
from us_contacts.views import about_us

urlpatterns = [
    path("", about_us, name="about")
]