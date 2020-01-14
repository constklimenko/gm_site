from rest_framework.viewsets import ModelViewSet

from .models import Artist, Genre, Painting, Place, Event, Article, Comment, Main
from .serializers import ArtistSerializer, GenreSerializer, PaintingSerializer, PlaceSerializer, \
    EventSerializer, ArticleSerializer, CommentSerializer, MainSerializer


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
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ApiMainViewSet(ModelViewSet):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


class ApiCommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
