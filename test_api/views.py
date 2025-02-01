from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from .serializers import GroupSerializer
from rest_framework.generics import GenericAPIView, ListCreateAPIView
from rest_framework.mixins import ListModelMixin


@api_view()
def hello_world(request):
    return Response({'message': 'Hello World!'})


class GroupListAPIView(ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    

    