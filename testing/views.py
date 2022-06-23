from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import *
from .models import *
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def total_students(self, request):
        user_count = Student.objects.count()
        return Response(user_count)

