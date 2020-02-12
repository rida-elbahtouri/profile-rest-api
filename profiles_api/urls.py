from django.urls import path,include
from rest_framework import routers
from .views import HelloApiView,UserViewSet,UserLoginApiVeiw,FeedItemViewSet

routers=routers.DefaultRouter()
routers.register('profiles',UserViewSet)
routers.register('feed',FeedItemViewSet)
urlpatterns = [
    path('hello',HelloApiView.as_view()),
    path('',include(routers.urls)),
    path('login/',UserLoginApiVeiw.as_view())
]
