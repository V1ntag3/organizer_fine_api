from django.db import transaction
from django.contrib.auth import login

from rest_framework import generics, viewsets, permissions
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.auth import TokenAuthentication
from knox.settings import CONSTANTS

from .models import RevenueSpending
from .serializers import RevenueSpendingSerializer, UserSerializer, RegisterSerializer

from datetime import datetime


import calendar
# Login API


class LoginAPI(KnoxLoginView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        # ṕrint(request.data['username'])
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)

# Register API


class RegisterAPI(generics.GenericAPIView):

    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

# Verificar usuário pelo Token


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user

# regata id do usuario pelo token


def get_user_from_token(token):
    objs = AuthToken.objects.filter(token_key=token[6:14])
    if len(objs) == 0:
        return None
    return objs.first().user.id

# salva de maneira segura de acordo com o login que foi utilizado


class RevenueSpendingView(viewsets.ModelViewSet):

    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    queryset = RevenueSpending.objects.all()
    serializer_class = RevenueSpendingSerializer

    def get_queryset(self):
        meses = [
        'Janeiro',
        'Fevereiro',
        'Março',
        'Abril',
        'Maio',
        'Junho',
        'Julho',
        'Agosto',
        'Setembro',
        'Outubro',
        'Novembro',
        'Dezembro',
    ]
        queryset = self.queryset
        
        minDate = str(self.request.GET['year']) + '-' + str(meses.index(self.request.GET['month'])+1) + '-01 ' + '00:00'
        
        maxDate = str(self.request.GET['year']) + '-' + str(meses.index(self.request.GET['month'])+1) + '-' + str(calendar.monthrange(int(self.request.GET['year']) , int(meses.index(self.request.GET['month'])+1))[1]) + ' 23:59'
        
        query_set = queryset.filter(user=get_user_from_token(
            self.request.headers['Authorization']), date__gte=minDate, date__lte=maxDate).order_by('-date')
        return query_set

    def create(self, request):
        request.data['user'] = get_user_from_token(
            self.request.headers['Authorization'])
        request.data['date'] = datetime.now()
        serializer = self.get_serializer(
            data=request.data, context={'request': request}, partial=True)
        serializer.is_valid(raise_exception=True)
        with transaction.atomic():
            event = serializer.save()
        serializer_response = RevenueSpendingSerializer(
            event, many=False
        )
        return Response(
            data=serializer_response.data,
        )

    def update(self, request, *args, **kwargs):
        request.data['user'] = get_user_from_token(self.request.headers['Authorization'])
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)