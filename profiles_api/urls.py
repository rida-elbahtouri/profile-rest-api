from django.urls import path,include
from rest_framework import routers
from .views import HelloApiView,UserViewSet

routers=routers.DefaultRouter()
routers.register('profiles',UserViewSet)

urlpatterns = [
    path('hello',HelloApiView.as_view()),
    path('',include(routers.urls))
]
