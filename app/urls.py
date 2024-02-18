from django.urls import path
from . import views

urlpatterns = [
    path('', views.create_new_user, name="create_new_user"),
    path('<str:id>/', views.send_new_message, name="send_new_message"),
    path('<str:id>/<str:pin>/', views.view_messages, name="view_messages"),
]