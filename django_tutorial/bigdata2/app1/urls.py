
from django.urls import path
from . import views

app_name = 'app1'
urlpatterns = [
    path('', views.first_page, name="first"),
    path('second/', views.second_page, name="second"),
]
