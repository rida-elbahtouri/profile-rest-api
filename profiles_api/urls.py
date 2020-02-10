from django.urls import path,include
from rest_framework import routers
from .views import HelloApiView,UserViewSet,UserLoginApiVeiw

routers=routers.DefaultRouter()
routers.register('profiles',UserViewSet)

urlpatterns = [
    path('hello',HelloApiView.as_view()),
    path('',include(routers.urls)),
    path('login/',UserLoginApiVeiw.as_view())
]
