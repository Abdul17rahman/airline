from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('<int:id>', views.flight, name="flight"),
    path('add/', views.add, name="add"),
    path('<int:id>/book', views.book, name="book"),
    path('<int:flight_id>/remove/<int:pass_id>/', views.remove, name="remove")
]