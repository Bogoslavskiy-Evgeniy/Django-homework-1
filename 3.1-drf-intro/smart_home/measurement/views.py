# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView


from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, CreateAPIView, UpdateAPIView


from .models import Sensor, Measurement
from .serializers import SensorDetailSerializer, SensorSerializer, MeasurementSerializer, SensorUpdateSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorView(RetrieveAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementsView(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


class UpdateSensor(UpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorUpdateSerializer
