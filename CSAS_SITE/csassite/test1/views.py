from django.shortcuts import render
from .models import posturl
# Create your views here.

def url_show(request):
    url_name = posturl.objects.all()
    return render(request, "test1/urlname.html", {"url_name": url_name})
