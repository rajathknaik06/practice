from django.urls import path

from .views import (
    HelloWorldView,
    PostListCreateView,
    PostDetailView
)

urlpatterns = [

    path(
        'hello/',
        HelloWorldView.as_view()
    ),

    path(
        'posts/',
        PostListCreateView.as_view()
    ),

    path(
        'posts/<int:pk>/',
        PostDetailView.as_view()
    ),
]