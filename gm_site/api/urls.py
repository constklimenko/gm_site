from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import ApiArtistViewSet, ApiCommentViewSet, ApiArticleViewSet, \
    ApiEventViewSet, ApiPlaceViewSet, ApiPaintingViewSet, ApiGenreViewSet, ApiMainViewSet

router = DefaultRouter()
router.register('artists', ApiArtistViewSet, basename='artists')
router.register('genres', ApiGenreViewSet, basename='genres')
router.register('paintings', ApiPaintingViewSet, basename='paintings')
router.register('places', ApiPlaceViewSet, basename='places')
router.register('events', ApiEventViewSet, basename='events')
router.register('articles', ApiArticleViewSet, basename='articles')
router.register('comments', ApiCommentViewSet, basename='comments')
router.register('main', ApiMainViewSet, basename='main')

urlpatterns = [
    path('', include(router.urls))
]
