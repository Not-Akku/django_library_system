from . import views
from django.urls import path

urlpatterns = [
    path('lend/', views.lend, name='lend'),
    path('return/', views.return_book, name='return_book'),
    path('fine/', views.fine, name='fine')
]