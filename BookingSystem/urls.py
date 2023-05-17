from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/', views.book, name='book'),
    path('search/', views.search, name='search'),
    path('manage/', views.manage_booking, name='manage')
]
