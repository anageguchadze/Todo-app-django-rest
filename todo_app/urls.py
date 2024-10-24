from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.contrib import admin
from .views import TodoView

router = DefaultRouter()
router.register(r'todos', TodoView)

urlpatterns = [
    path('', include(router.urls))
]