from rest_framework import viewsets
from .serializers import *
from .models import *


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer


class CoursesViewSet(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class FeedbacksViewSet(viewsets.ModelViewSet):
    queryset = Feedbacks.objects.all()
    serializer_class = FeedbacksSerializer


class TechnicalSupportViewSet(viewsets.ModelViewSet):
    queryset = TechnicalSupport.objects.all()
    serializer_class = TechnicalSupportSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class TrainingScheduleViewSet(viewsets.ModelViewSet):
    queryset = TrainingSchedule.objects.all()
    serializer_class = TrainingScheduleSerializer
