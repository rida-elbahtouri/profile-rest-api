from django.urls import path
from .views import HelloApiView

urlpatterns = [
    path('hello',HelloApiView.as_view())
]
