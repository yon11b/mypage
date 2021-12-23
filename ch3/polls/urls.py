from django.urls import path
from .import views

urlpatterns=[
    path('', views.index, name='index'),
    path('whoami/', views.intro, name='intro'),
    path('happyhackking/', views.context, name='context'),
]