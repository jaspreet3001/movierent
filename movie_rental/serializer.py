from rest_framework import serializers
from movie_rental import models

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.movie
        fields = ('name', 'year', 'lang')
