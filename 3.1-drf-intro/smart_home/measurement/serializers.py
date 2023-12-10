from rest_framework import serializers
from measurement.models import Measurement, Sensor

<<<<<<< HEAD
class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields =['sensor', 'temperature', 'created at']
=======
from measurement.models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature', 'created_at']

>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
<<<<<<< HEAD

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)
    class Meta:
        model =Sensor
        fields = ['id', 'name', 'description', 'measurements']
# TODO: опишите необходимые сериализаторы
=======
        

class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)    
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
>>>>>>> da34ece7ad16c6ca2ff424630ef67e03ef525b02
