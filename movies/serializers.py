from rest_framework import serializers
from genres.serializers import GenreSerializer
from .models import Movie
from genres.models import Genre


class MovieSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    def create(self, validated_data: dict):
        genre_data = validated_data.pop("genres")
        movie = Movie.objects.create(**validated_data)

        for value in genre_data:
            genre = Genre.objects.filter(name__iexact=value["name"]).first()

            if not genre:
                genre = Genre.objects.create(**value)

            movie.genres.add(genre)

        return movie

    class Meta:
        model = Movie
        fields = [
            "id",
            "title",
            "duration",
            "premiere",
            "budget",
            "overview",
            "genres",
        ]
