from rest_framework import serializers
from .models import Visita, Comentario
from django.contrib.auth.models import User

class VisitaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('id', 'nombre', 'descripción', 'likes', 'foto')


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comentario
        fields = ('visita', 'texto')

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class LikeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Visita
        fields = ('likes',)
