from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.index),            # Trang index hiển thị form
    path('weather_api/', views.weather), # API được gọi từ JS
]
