from django.urls import path
from .views import infoView,resultView


urlpatterns = [
    path('',infoView),
    path('result/',resultView),
]
