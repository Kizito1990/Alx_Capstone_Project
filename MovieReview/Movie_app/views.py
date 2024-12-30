from rest_framework import viewsets, permissions, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Review, User, Like
from .serializers import ReviewSerializer, UserSerializer, LikeSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['movie_title']
    ordering_fields = ['rating', 'created_at']
    


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]
#Validating Likes, making sure a user cannot like posts twice
    def create(self, request, *args, **kwargs):
        review_id = request.data.get("review")
        review = Review.objects.get(id=review_id)
        like, created = Like.objects.get_or_create(user=request.user, review=review)
        if not created:
            return Response({"detail": "You already liked this review."}, status=400)
        return Response({"detail": "Review liked."})