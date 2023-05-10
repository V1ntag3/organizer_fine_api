from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication

from rest_framework import generics, viewsets, permissions

from .models import RevenueSpending
from .serializers import RevenueSpendingSerializer, UserSerializer, RegisterSerializer

from rest_framework.permissions import AllowAny, IsAuthenticated

from django.contrib.auth import login

# Login API
class LoginAPI(KnoxLoginView):
    
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Register API
class RegisterAPI(generics.GenericAPIView):
    
    serializer_class = RegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })


class RevenueSpendingView(viewsets.ModelViewSet):
    
    authentication_classes = (TokenAuthentication,)
    permission_classes = (AllowAny,)
    
    queryset = RevenueSpending.objects.all()
    serializer_class = RevenueSpendingSerializer

    def get_queryset(self):
        queryset = self.queryset
        query_set = queryset.filter(user=self.request.GET['id'])
        return query_set
