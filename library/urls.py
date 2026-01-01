from . import views
from django.urls import path

urlpatterns = [
    path('lend/',views.lend, name="lend")
]