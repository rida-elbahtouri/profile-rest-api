from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,viewsets,filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from .serializers import HelloSerializer,UserSerializer
from  .models import UserProfile
from .permissions import UpdateOwnProfile

class HelloApiView(APIView):
    """test apiview"""
    serializer_class=HelloSerializer

    def get(self,request,format=None):
        """return a list of ApiViews featurs"""
        an_apiview=[
            'Uses HTTP method as function (get, post, patch, put, delete)',
            'Is similar to django view',
            'gives you the most control over your app',
            'Is mapped manualy to Urls',
        ]
        return Response({'msg':'hello','an_apiview':an_apiview})

    def post(self,request):
        """create a hello msg with our name"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            msag=f'hello {name}'
            return Response({'msag':msag})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk=None):
        """handel updatin data"""
        return Response({'method':'PUT'})
    def patch(self,request,pk=None):
        """handel a partial update of an object"""
        return Response({'method':'PARCH'})
    def delete(self,request,pk=None):
        """Delete an object"""
        return Response ({'method':'DELETE'})

class UserViewSet(viewsets.ModelViewSet):
    """handel creating and updation viewset"""
    serializer_class = UserSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields=('First_name','Last_name','email',)

class UserLoginApiVeiw(ObtainAuthToken):
    """handel creating user authonication tokens"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
