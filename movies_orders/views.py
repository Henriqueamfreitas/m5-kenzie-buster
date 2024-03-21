from rest_framework.views import APIView, Request, Response, status
from rest_framework_simplejwt.authentication import JWTAuthentication
from movies.models import Movie
from .serializers import MovieOrderSerializer
from rest_framework.exceptions import AuthenticationFailed


# Create your views here.
class MovieOrderView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request, movie_id: int) -> Response:
        if not request.user.is_authenticated:
            raise AuthenticationFailed(detail="Authentication credentials were not provided.")

        try:
            found_movie = Movie.objects.get(pk=movie_id)
        except Movie.DoesNotExist:
            return Response({'message': 'Movie not found'}, status.HTTP_404_NOT_FOUND)

        serializer = MovieOrderSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save(user=request.user, movie=found_movie)  
        return Response(serializer.data, status.HTTP_201_CREATED)
