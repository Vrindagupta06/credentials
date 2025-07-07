from django.urls import path
from .views import create_login, update_login, login_list, delete_login

urlpatterns = [
    path('', login_list, name= "list"),
    path('create/', create_login, name="create"),
    path('update/<int:pk>/', update_login, name="update"),
    path('delete/<int:pk>/', delete_login, name="delete")
]
