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