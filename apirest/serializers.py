from rest_framework import serializers
from core.models import PerfilUsuario, Producto
from django.contrib.auth.models import User

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'

class UserTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email','first_name','last_name')

class USuscriptorSerializer(serializers.ModelSerializer):
    user = UserTokenSerializer(many = False, read_only = True)
    class Meta:
        model = PerfilUsuario
        fields =('es_suscriptor','user')
        read_only_fields =('user',)
        
        

