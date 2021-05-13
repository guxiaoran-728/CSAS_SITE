from django.conf.urls import url
from . import views

urlpatterns = [
    url('name/', views.url_show, name="url_show"),
]
