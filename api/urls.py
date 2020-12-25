# First-party
from .views import TopicViewSet, CommentViewSet, LikeDislikeViewSet, UserViewSet
# Django
from django.urls import include, path
# Third-party
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likesdislikes', LikeDislikeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]