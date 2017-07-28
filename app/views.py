# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from .serializers import UserRegistrationSerializer,UserAuthenticationSerializer, PersonRegistrationSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated

# Create your views here
class UserRegistrationView(APIView):
    """
    Register a new User

    """
    serializer_class = UserRegistrationSerializer

    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UserAuthenticationView(APIView):
    '''
    Authentication View.
    '''
    serializer_class = UserAuthenticationSerializer
    def post(self,request,*args,**kwargs):
        serializer=self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            return Response({'token':user.auth_token.key},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)

class PersonRegistrationView(APIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = PersonRegistrationSerializer
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=self.request.data)
        if serializer.is_valid():
            return Response(status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_401_UNAUTHORIZED)




