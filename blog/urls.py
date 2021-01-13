from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('<int:blog_id>/', views.details, name='details'),

]