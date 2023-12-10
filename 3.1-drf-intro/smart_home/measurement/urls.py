from django.urls import path

from measurement.views import MeasurementViewSet, SensorDetailViewSet, SensorViewSet
<<<<<<< HEAD
urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
=======

urlpatterns = [
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
    path('sensors/', SensorViewSet.as_view({'get': 'list'})),
    path('sensors/', SensorViewSet.as_view({'post': 'create'})),
    path('sensors/<pk>/', SensorDetailViewSet.as_view()),
    path('measurements/', MeasurementViewSet.as_view({'post': 'create'})),
<<<<<<< HEAD
]
=======
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
