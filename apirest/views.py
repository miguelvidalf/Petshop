from django.shortcuts import render
from django.contrib.sessions.models import Session 
from datetime import datetime

from django.shortcuts import render
from django.http import response
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse_lazy

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import *
from core.models import Producto, PerfilUsuario

# Create your views here.

class producto_create(APIView):
    def post(self, request , format = None):
        serializer = ProductoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

class producto_update(APIView):
    def put(self, request, format=None):
        serializer = ProductoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.update()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def producto_read(request, id):
    if request.method == 'GET':
        objeto = get_object_or_404(Producto, idProducto=id)
        serializer = ProductoSerializer(objeto)
        return Response(serializer.data)

@csrf_exempt
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def producto_read_all(request):
    if request.method == 'GET':
        list = Producto.objects.all().order_by('idProducto')
        serializer = ProductoSerializer(list, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def producto_delete(request, id):
    if request.method == 'DELETE':
        try:
            Producto.objects.get(idProducto=id).delete()
            return Response({'mensaje':"Se elimino el producto"},status=status.HTTP_204_NO_CONTENT)
        except Producto.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class Login(ObtainAuthToken):
    def post(self,request,*arg,**kwargs):
        login_serializer = self.serializer_class(data= request.data, context = {'request': request})
        if login_serializer.is_valid():
            user = login_serializer.validated_data['user']
            if user.is_active:
                token, created = Token.objects.get_or_create(user = user)
                user_serializer = UserTokenSerializer(user)
                if created:
                    return Response({
                        'token': token.key, 
                        'user': user_serializer.data, 
                        'mensaje': 'Inicio sesión exitoso'}
                        , status=status.HTTP_201_CREATED)
                else:
                    all_sessions = Session.objects.filter(expire_date__gte = datetime.now())
                    if all_sessions.exists():
                        for session in all_sessions:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()
                    token.delete()
                    token = Token.objects.create(user = user)
                    return Response({
                        'token': token.key, 
                        'user': user_serializer.data, 
                        'mensaje': 'Inicio sesión exitoso'}
                        , status=status.HTTP_201_CREATED)
            else: 
                return Response({'error':'Usuario invalido'}, status= status.HTTP_401_UNAUTHORIZED)
        else:
            print("hola")
            return Response({'error': 'Nombre de usuario o contraseña incorrectas'}, status= status.HTTP_400_BAD_REQUEST)