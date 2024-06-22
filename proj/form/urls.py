# from django.contrib import admin
# from django.urls import path
# from . import views
# urlpatterns = [
#     path("", views.index),
# ]

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('farmer_form', views.farmer_form, name='farmer_form'),
]
