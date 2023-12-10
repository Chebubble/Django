# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
import statistics
from django.http import JsonResponse
from rest_framework import generics, viewsets

from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import MeasurementSerializer, SensorDetailSerializer, SensorSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
<<<<<<< HEAD

=======
    
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
    def post(self, request):
        data = request.data
        Sensor.objects.create(name=data.get('name'), description=data.get('description'))
        return Response(data=data)
<<<<<<< HEAD


class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
=======
    
    
    
class MeasurementViewSet(viewsets.ModelViewSet):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer  
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02

    def post(self, request):
        data = request.data
        Measurement.objects.create(sensor=data.get('sensor'), temperature=data.get('temperature'))
        return Response(data=data)

<<<<<<< HEAD

class SensorDetailViewSet(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

=======
class SensorDetailViewSet(generics.RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer  
    
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
    def patch(self, request, pk):
        data = request.data
        name, description = data.get('name'), data.get('description')
        sensor = Sensor.objects.filter(id=pk).all()
        if name:
            sensor.update(name=name)
        if description:
            sensor.update(description=description)
<<<<<<< HEAD
        return Response(data=data)
=======
        return Response(data=data)  
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
