from django.shortcuts import render

# Create your views here.
from rest_framework import generics, viewsets
from CRUD.models import student
from .serialziers import StudentSerializer
from rest_framework.response import Response

class StudentList(generics.ListCreateAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer 

class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

    def put(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer