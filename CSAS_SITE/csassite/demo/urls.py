from django.urls import path
from . import views
urlpatterns = [
    path('py',views.Main.as_view(),name='main')
]
