# from django.shortcuts import render
from rest_framework import viewsets
from PersonalDashboard_api.serializers import PersonalMemoSerializer
from PersonalDashboard_api.models import PersonalMemo

# Create your views here.
class PersonalMemoViewSet(viewsets.ModelViewSet):
   queryset = PersonalMemo.objects.all()
   serializer_class = PersonalMemoSerializer