from rest_framework.viewsets import ModelViewSet

from .models import Artist, Genre, Painting, Place, Event, Article, Comment
from .serializers import ArtistSerializer, GenreSerializer, PaintingSerializer, PlaceSerializer, \
    EventSerializer, ArticleSerializer, CommentSerializer


class ApiArtistViewSet(ModelViewSet):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer


class ApiGenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class ApiPaintingViewSet(ModelViewSet):
    queryset = Painting.objects.all()
    serializer_class = PaintingSerializer


class ApiPlaceViewSet(ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer


class ApiEventViewSet(ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class ApiArticleViewSet(ModelViewSet):
    queryset = Article.objects.filter(for_main=False)
    serializer_class = ArticleSerializer


class ApiCommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
