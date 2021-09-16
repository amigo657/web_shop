from django.shortcuts import render

def price_page(request):
    return render(request, "price.html", {})
