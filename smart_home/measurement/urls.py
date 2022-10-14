from django.contrib import admin
from django.urls import path

from measurement.views import SensorsView, UpdateSensorsView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('measurements/', MeasurementView.as_view()),
    path('sensors/<pk>/', UpdateSensorsView.as_view()),
]