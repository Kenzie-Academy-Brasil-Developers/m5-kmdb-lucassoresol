from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsUserCreateReview
from movies.models import Movie
from .models import Review
from .serializers import ReviewSerializer


class ReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsUserCreateReview]

    def perform_create(self, serializer):
        movie = get_object_or_404(Movie, id=self.kwargs["movie_id"])
        return serializer.save(
            movie=movie,
            critic=self.request.user,
        )
