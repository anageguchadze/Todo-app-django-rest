from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from .views import AuthorViewSet, PostViewSet 

router = DefaultRouter()
router.register(r'authors', AuthorViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]