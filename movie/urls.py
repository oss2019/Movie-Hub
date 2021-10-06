from django.urls import path
from . import views
urlpatterns = [
    path('search', views.search, name='search'),
    path('movieinfo/<int:item_id>/', views.movieinfo, name='movieinfo'),
    path('checkout', views.checkout, name='checkout')
]
