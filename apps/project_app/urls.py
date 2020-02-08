from django.urls import path
from . import views
# from .views import user_list

urlpatterns = [
    path('', views.index, name='index'),
    # path('<str:room_name>/', views.room, name="room"),
    # path('register', views.register),
]