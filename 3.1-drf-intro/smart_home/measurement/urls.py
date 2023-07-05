from django.urls import path

from measurement.views import MeasurementViewSet, SensorDetailViewSet, SensorViewSet

urlpatterns = [
    path('sensors/', SensorViewSet.as_view({'get': 'list'})),
    path('sensors/', SensorViewSet.as_view({'post': 'create'})),
    path('sensors/<pk>/', SensorDetailViewSet.as_view()),
    path('measurements/', MeasurementViewSet.as_view({'post': 'create'})),
