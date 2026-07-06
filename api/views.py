from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend

from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly


class HelloWorldView(APIView):

    def get(self, request):
        return Response(
            {"message": "Hello REST API"},
            status=status.HTTP_200_OK
        )


class PostListCreateView(generics.ListCreateAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]

    filterset_fields = {
        'owner__username': ['exact'],
        'created_at': ['year', 'month', 'day', 'gt', 'lt']
    }

    search_fields = [
        'title',
        'content',
        'owner__username'
    ]

    ordering_fields = [
        'created_at',
        'title',
        'owner__username'
    ]

    ordering = [
        '-created_at'
    ]

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )


class PostDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Post.objects.all()

    serializer_class = PostSerializer

    permission_classes = [
        IsOwnerOrReadOnly
    ]