from django.urls import path

from measurement.views import SensorCreateView, sensor_create_view, SensorUpdate, AddMeasurement

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorCreateView.as_view()),
    # path('sensors/', sensor_create_view),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    path('measurements/', AddMeasurement.as_view()),
]
