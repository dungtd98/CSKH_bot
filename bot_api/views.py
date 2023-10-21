from django.shortcuts import render
from rest_framework.views import APIView
from .models import BotModel
from .serializers import BotSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from uuid import UUID
# Create your views here.

class BotListView(APIView):
    def get(self, request, format=None, *args, **kwargs):
        queryset = BotModel.objects.all()
        serializer = BotSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request, format=None, *args, **kwargs):
        serializer = BotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BotDetailView(APIView):
    def _get_object(self, id):
        # uuid_obj = UUID(id)
        print(id)
        try:
            return BotModel.objects.get(id = UUID(id))
        except BotModel.DoesNotExist:
            raise Http404
    def get(self, request, id, *args, **kwargs):
        instance = self._get_object(id)
        serializer = BotSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def patch(self, request, id, *args, **kwargs):
        instance = self._get_object(id)
        serializer = BotSerializer(instance,data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id, *args, **kwargs):
        instance = self._get_object(id)
        instance.delete()
        return Response({'detail':'Delete Success'}, status=status.HTTP_204_NO_CONTENT)