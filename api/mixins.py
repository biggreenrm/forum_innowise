from rest_framework.decorators import action
from rest_framework.response import Response

from likedislike import services
from .serializers import UserSerializer


class LikedDislikedMixin:

    @action(detail=True, methods=['POST'])
    def like(self, request, pk=None):
        """Like object"""
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(detail=True, methods=['POST'])
    def dislike(self, request, pk=None):
        """Dislike object"""
        obj = self.get_object()
        services.add_dislike(obj, request.user)
        return Response()
    
    @action(detail=True, methods=['POST'])
    def unlike(self, request, pk=None):
        """Remove likedislike object"""
        obj = self.get_object()
        services.remove_like_dislike(obj, request.user)
        return Response()

    @action(detail=True, methods=['GET'])
    def liked_persons(self, request, pk=None):
        """Получает всех пользователей, которые лайкнули `obj`."""
        obj = self.get_object()
        liked_persons = services.get_liked_persons(obj)
        serializer_context = {
            'request': request,
        }
        serializer = UserSerializer(liked_persons, many=True, context=serializer_context)
        return Response(serializer.data)    