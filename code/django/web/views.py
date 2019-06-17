from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from web.serializers import *
from web.models import Dollar


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class DollarViewSet(viewsets.ModelViewSet):
    queryset = Dollar.objects.all()
    serializer_class = DollarSerializer

    def get_queryset(self):
        date_start = self.request.query_params.get('date_start', None)
        date_end = self.request.query_params.get('date_end', None)
        if date_start and date_end:
            return self.queryset.filter(value_at__range=[date_start, date_end])
        else:
            return self.queryset