from django.urls import path

from measurement.views import SensorsView, SensorView, MeasurementsView, UpdateSensor

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensor/<pk>/', SensorView.as_view()),
    path('measurements/', MeasurementsView.as_view()),
    path('sensors/<pk>/', UpdateSensor.as_view())
]
