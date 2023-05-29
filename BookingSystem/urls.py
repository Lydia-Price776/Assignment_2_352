from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book_flight/', views.book, name='book'),
    path('search_results/', views.search, name='search'),
    path('view_booking/', views.manage_booking, name='view'),
    path('cancel_booking/', views.cancel_booking, name='cancel')

]
