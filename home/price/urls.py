from django.urls import path
from price.views import price_page

urlpatterns = [
    path("", price_page, name="work_prices")
]
