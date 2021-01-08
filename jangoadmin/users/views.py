from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import exceptions

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import JSONRenderer

# Create your views here.
from kuldeep.models import Harvest, Bread
from . serializers import HarvestSerializer, BreadSerializer

class HarvestAPIView(APIView):
    """
    Create A Post and Get Api for Harvest.
    """
    serializer_class = HarvestSerializer
    permission_classes = [AllowAny,]
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        try:
            harvest_data = Harvest.objects.all()
            serializer = HarvestSerializer(harvest_data, many=True)
            return Response({"data":serializer.data, "status":200})
        except Exception as error:
            print(error)
            return Response({"msg":"Invalid Response","status":422})

    def post(self, request):
        data = request.data
        serializer = HarvestSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"success","status":200})
        else:
            return Response({"msg":"Invalid Request","status":422})



class BreadAPIView(APIView):
    """
    Create A Post and Get Api for Harvest.
    """
    serializer_class = BreadSerializer
    permission_classes = [AllowAny,]
    renderer_classes = (JSONRenderer,)

    def get(self, request):
        try:
            harvest_data = Bread.objects.all()
            serializer = BreadSerializer(harvest_data, many=True)
            return Response({"data":serializer.data, "status":200})
        except Exception as error:
            print(error)
            return Response({"msg":"Invalid Response","status":422})

    def post(self, request):
        data = request.data
        serializer = BreadSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"success","status":200})
        else:
            return Response({"msg":"Invalid Request","status":422})



class HarvestViewSet(viewsets.ModelViewSet):
    queryset = Harvest.objects.all()
    serializer_class = HarvestSerializer


class BreadViewSet(viewsets.ModelViewSet):
    queryset = Bread.objects.all()
    serializer_class = BreadSerializer
