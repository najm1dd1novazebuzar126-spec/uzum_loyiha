from django.urls import path
from .views import tovarr

urlpatterns = [
    path('tovarr/', tovarr, name= 'tovarr'),
]