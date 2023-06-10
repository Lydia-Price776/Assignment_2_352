from django.urls import path
from . import views

# Url paths for each page
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book_flight/', views.book, name='book'),
    path('search_results/', views.search, name='search'),
    path('view_booking/', views.view_booking, name='view'),
    path('cancel_booking/', views.cancel_booking, name='cancel')

]
