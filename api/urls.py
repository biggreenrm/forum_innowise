# First-party
from .views import TopicViewSet, CommentViewSet, LikeDislikeViewSet, UserViewSet
# Django
from django.urls import include, path
# Third-party
from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views


router = routers.DefaultRouter()
router.register(r'topics', TopicViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'likesdislikes', LikeDislikeViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-auth/', include('rest_framework.urls')),
]