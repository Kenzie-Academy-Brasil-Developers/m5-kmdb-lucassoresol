from rest_framework import generics
from users.permissions import IsAdminUserCreate
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Movie
from .serializers import MovieSerializer


class MovieView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminUserCreate]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
