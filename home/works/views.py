from django.shortcuts import render

def our_works(request):
    return render(request, "works.html", {})