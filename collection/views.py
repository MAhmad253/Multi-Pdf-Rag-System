from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# In this we import the models and serilizers 
from .models import Collections
from .serializers import CollectionsSerializers

class CollectionListCreateView(generics.ListCreateAPIView):
    serializer_class = CollectionsSerializers
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        return Collections.objects.filter(
            user=self.request.user
        )
    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )