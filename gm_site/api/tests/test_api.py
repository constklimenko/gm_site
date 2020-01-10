import datetime
import json

from django.core.serializers.json import DjangoJSONEncoder
from django.test import TestCase, Client
from django.urls import reverse
from rest_framework import status

from ..models import Artist, Genre, Place, Painting, Event, Article, Comment
from ..serializers import ArtistSerializer, GenreSerializer, PlaceSerializer, PaintingSerializer, EventSerializer, \
    ArticleSerializer, CommentSerializer

client = Client()


class ApiGenreTest(TestCase):
    def setUp(self) -> None:
        self.landscape = Genre.objects.create(genre_name="Пейзаж")
        self.still_live = Genre.objects.create(genre_name="Натюрморт")

    def test_get_genres(self):
        response = client.get(reverse('genres-list'))
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_genre(self):
        response = client.get(reverse('genres-detail', kwargs={'pk': self.landscape.pk}))
        serializer = GenreSerializer(self.landscape, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_genre(self):
        response = client.delete(reverse('genres-detail', kwargs={'pk': self.landscape.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('genres-detail', kwargs={'pk': self.landscape.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_genre(self):
        valid_genre = {
            'genre_name': 'Портрет'
        }
        response = client.post(reverse('genres-list'),
                               data=json.dumps(valid_genre, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_genre(self):
        invalid_genre = {
            'name_genre': 'Портрет'
        }
        response = client.post(reverse('genres-list'),
                               data=json.dumps(invalid_genre, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_genre(self):
        valid_genre = {
            'genre_name': 'Городской пейзаж'
        }
        response = client.put(reverse('genres-detail', kwargs={'pk': self.landscape.pk}),
                              data=json.dumps(valid_genre, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Genre.objects.get(pk=self.landscape.pk).genre_name, 'Городской пейзаж')

    def test_invalid_update_genre(self):
        invalid_genre = {
            'name_genre': 'Портрет'
        }
        response = client.put(reverse('genres-detail', kwargs={'pk': self.landscape.pk}),
                              data=json.dumps(invalid_genre, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Genre.objects.get(pk=self.landscape.pk).genre_name, 'Пейзаж')


class ApiArtistTest(TestCase):
    def setUp(self) -> None:
        self.rembrandt = Artist.objects.create(name='Рембрандт Харменс ван Рейн',
                                               is_master=True,
                                               artist_date=datetime.date(1606, 7, 15))
        self.dau = Artist.objects.create(name='Герард Дау',
                                         is_master=False,
                                         artist_date=datetime.date(1613, 4, 7))

    def test_get_artists(self):
        response = client.get(reverse('artists-list'))
        artists = Artist.objects.all()
        serializer = ArtistSerializer(artists, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_artist(self):
        response = client.get(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}))
        serializer = ArtistSerializer(self.rembrandt, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_genre(self):
        response = client.delete(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_genre(self):
        valid_artist = {
            'is_master': True,
            'name': 'Михаил Гладких',
            'artist_date': datetime.date(1968, 4, 29)
        }
        response = client.post(reverse('artists-list'),
                               data=json.dumps(valid_artist, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_genre(self):
        invalid_artist = {
            'is_master': False,
            'artist_name': 'Владислав Пегов'
        }
        response = client.post(reverse('artists-list'),
                               data=json.dumps(invalid_artist, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_genre(self):
        valid_artist = {
            'is_master': True,
            'name': 'Рембрандт',
            'artist_date': datetime.date(1606, 7, 15)
        }

        response = client.put(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}),
                              data=json.dumps(valid_artist, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Artist.objects.get(pk=self.rembrandt.pk).name, 'Рембрандт')

    def test_invalid_update_genre(self):
        invalid_genre = {
            'is_master': True,
            'artist_name': 'Рембрандт',
            'artist_date': datetime.date(1606, 7, 15)
        }
        response = client.put(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}),
                              data=json.dumps(invalid_genre, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Artist.objects.get(pk=self.rembrandt.pk).name, 'Рембрандт Харменс ван Рейн')


class ApiPlaceTest(TestCase):
    def setUp(self) -> None:
        self.izhad = Place.objects.create(name="Ижад")
        self.miras = Place.objects.create(name="Мирас")

    def test_get_places(self):
        response = client.get(reverse('places-list'))
        places = Place.objects.all()
        serializer = PlaceSerializer(places, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_place(self):
        response = client.get(reverse('places-detail', kwargs={'pk': self.izhad.pk}))
        serializer = PlaceSerializer(self.izhad, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_place(self):
        response = client.delete(reverse('places-detail', kwargs={'pk': self.izhad.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('places-detail', kwargs={'pk': self.izhad.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_place(self):
        valid_place = {
            'name': 'Знания'
        }
        response = client.post(reverse('places-list'),
                               data=json.dumps(valid_place, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_place(self):
        invalid_place = {
            'name_place': 'Знания'
        }
        response = client.post(reverse('places-list'),
                               data=json.dumps(invalid_place, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_place(self):
        valid_place = {
            'name': 'выстовочный зал "Ижад"'
        }
        response = client.put(reverse('places-detail', kwargs={'pk': self.izhad.pk}),
                              data=json.dumps(valid_place, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Place.objects.get(pk=self.izhad.pk).name, 'выстовочный зал "Ижад"')

    def test_invalid_update_genre(self):
        invalid_place = {
            'name_place': 'выстовочный зал "Ижад"'
        }
        response = client.put(reverse('places-detail', kwargs={'pk': self.izhad.pk}),
                              data=json.dumps(invalid_place, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Place.objects.get(pk=self.izhad.pk).name, 'Ижад')


class ApiPaintingTest(TestCase):
    def setUp(self):
        self.rembrandt = Artist.objects.create(name='Рембрандт Харменс ван Рейн',
                                               is_master=True,
                                               artist_date=datetime.date(1606, 7, 15))
        self.dau = Artist.objects.create(name='Герард Дау',
                                         is_master=False,
                                         artist_date=datetime.date(1613, 4, 7))
        self.landscape = Genre.objects.create(genre_name='Пейзаж')
        self.still_live = Genre.objects.create(genre_name='Натюрморт')
        self.allegory_of_music \
            = Painting.objects.create(title='Аллегория музыки',
                                      author=self.rembrandt,
                                      painting_date=0)
        self.allegory_of_music.genres.add(self.landscape.pk, self.still_live.pk)
        self.allegory_of_music.save()
        self.hermit = Painting.objects.create(title='Отшельник',
                                              author=self.dau,
                                              painting_date=0)
        self.hermit.genres.add(self.still_live.pk)
        self.hermit.save()

    def test_get_paintings(self):
        response = client.get(reverse('paintings-list'))
        paintings = Painting.objects.all()
        serializer = PaintingSerializer(paintings, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_painting(self):
        response = client.get(reverse('paintings-detail', kwargs={'pk': self.allegory_of_music.pk}))
        serializer = PaintingSerializer(self.allegory_of_music, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_painting(self):
        response = client.delete(reverse('paintings-detail',
                                         kwargs={'pk': self.allegory_of_music.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('paintings-detail', kwargs={'pk': self.allegory_of_music.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = client.get(reverse('artists-detail', kwargs={'pk': self.rembrandt.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_painting(self):
        valid_painting = {
            'title': 'Ночной дозор',
            'author': self.rembrandt.pk,
            'genres': [self.landscape.pk, self.still_live.pk]
        }
        response = client.post(reverse('paintings-list'),
                               data=json.dumps(valid_painting, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Painting.objects.get(title='Ночной дозор').author.name,
                         'Рембрандт Харменс ван Рейн')

    def test_create_invalid_painting(self):
        invalid_place = {
            'name': 'Ночной дозор',
            'author': self.rembrandt.pk,
            'genres': [self.landscape.pk, self.still_live.pk]
        }
        response = client.post(reverse('paintings-list'),
                               data=json.dumps(invalid_place, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_painting(self):
        valid_place = {
            'title': 'Аллегория музыки',
            'author': self.dau.pk,
            'genres': [self.landscape.pk, self.still_live.pk]
        }
        response = client.put(reverse('paintings-detail', kwargs={'pk': self.allegory_of_music.pk}),
                              data=json.dumps(valid_place, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Painting.objects.get(pk=self.allegory_of_music.pk).author.name, 'Герард Дау')

    def test_invalid_update_genre(self):
        invalid_place = {
            'name': 'Аллегория музыки',
            'author': self.dau.pk,
            'genres': [self.landscape.pk, self.still_live.pk]
        }
        response = client.put(reverse('paintings-detail', kwargs={'pk': self.allegory_of_music.pk}),
                              data=json.dumps(invalid_place),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Painting.objects.get(pk=self.allegory_of_music.pk).author.name,
                         'Рембрандт Харменс ван Рейн')


class ApiEventTest(TestCase):
    def setUp(self):
        self.rembrandt = Artist.objects.create(name='Рембрандт Харменс ван Рейн',
                                               is_master=True,
                                               artist_date=datetime.date(1606, 7, 15))
        self.dau = Artist.objects.create(name='Герард Дау',
                                         is_master=False,
                                         artist_date=datetime.date(1613, 4, 7))
        self.landscape = Genre.objects.create(genre_name='Пейзаж')
        self.still_live = Genre.objects.create(genre_name='Натюрморт')
        self.allegory_of_music \
            = Painting.objects.create(title='Аллегория музыки',
                                      author=self.rembrandt,
                                      painting_date=0)
        self.allegory_of_music.genres.add(self.landscape.pk, self.still_live.pk)
        self.allegory_of_music.save()
        self.hermit = Painting.objects.create(title='Отшельник',
                                              author=self.dau,
                                              painting_date=0)
        self.hermit.genres.add(self.still_live.pk)
        self.hermit.save()
        self.izhad = Place.objects.create(name="Ижад")
        self.miras = Place.objects.create(name="Мирас")
        self.new_year = Event.objects.create(name='Новый год',
                                             place=self.izhad)
        self.christmas = Event.objects.create(name='Рождество',
                                              place=self.miras)

    def test_get_events(self):
        response = client.get(reverse('events-list'))
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_event(self):
        response = client.get(reverse('events-detail', kwargs={'pk': self.new_year.pk}))
        serializer = EventSerializer(self.new_year, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_event(self):
        response = client.delete(reverse('events-detail',
                                         kwargs={'pk': self.new_year.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('events-detail', kwargs={'pk': self.new_year.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = client.get(reverse('places-detail', kwargs={'pk': self.izhad.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_valid_event(self):
        valid_event = {
            'name': 'Хэллоуин',
            'place': self.izhad.pk,
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk]
        }
        response = client.post(reverse('events-list'),
                               data=json.dumps(valid_event, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Event.objects.get(name='Хэллоуин')
                         .artists.get(name='Герард Дау').pk, self.dau.pk)

    def test_create_invalid_event(self):
        invalid_event = {
            'event_name': 'Хэллоуин',
            'place': self.izhad.pk,
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk]
        }
        response = client.post(reverse('events-list'),
                               data=json.dumps(invalid_event, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_event(self):
        valid_event = {
            'name': 'Кошмар перед рождеством',
            'place': self.miras.pk,
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk]
        }
        response = client.put(reverse('events-detail', kwargs={'pk': self.christmas.pk}),
                              data=json.dumps(valid_event, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Event.objects.get(pk=self.christmas.pk).name, 'Кошмар перед рождеством')

    def test_invalid_update_event(self):
        invalid_event = {
            'event_name': 'Кошмар перед рождеством',
            'place': self.miras.pk,
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk]
        }
        response = client.put(reverse('events-detail', kwargs={'pk': self.christmas.pk}),
                              data=json.dumps(invalid_event, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Event.objects.get(pk=self.christmas.pk).name, 'Рождество')


class ApiArticleTest(TestCase):
    def setUp(self):
        self.rembrandt = Artist.objects.create(name='Рембрандт Харменс ван Рейн',
                                               is_master=True,
                                               artist_date=datetime.date(1606, 7, 15))
        self.dau = Artist.objects.create(name='Герард Дау',
                                         is_master=False,
                                         artist_date=datetime.date(1613, 4, 7))
        self.landscape = Genre.objects.create(genre_name='Пейзаж')
        self.still_live = Genre.objects.create(genre_name='Натюрморт')
        self.allegory_of_music \
            = Painting.objects.create(title='Аллегория музыки',
                                      author=self.rembrandt,
                                      painting_date=0)
        self.allegory_of_music.genres.add(self.landscape.pk, self.still_live.pk)
        self.allegory_of_music.save()
        self.hermit = Painting.objects.create(title='Отшельник',
                                              author=self.dau,
                                              painting_date=0)
        self.hermit.genres.add(self.still_live.pk)
        self.hermit.save()
        self.izhad = Place.objects.create(name="Ижад")
        self.miras = Place.objects.create(name="Мирас")
        self.new_year = Event.objects.create(name='Новый год',
                                             place=self.izhad)
        self.christmas = Event.objects.create(name='Рождество',
                                              place=self.miras)
        self.first_article = Article.objects.create(title='Первая статья',
                                                    content='Текст первой статьи')
        self.first_article.places.add(self.izhad.pk, self.miras.pk)
        self.first_article.artists.add(self.rembrandt.pk, self.dau.pk)
        self.second_article = Article.objects.create(title='Вторая статья',
                                                     content='Текст второй статьи')
        self.second_article.paintings.add(self.allegory_of_music.pk, self.hermit.pk)
        self.second_article.events.add(self.new_year.pk, self.christmas.pk)

    def test_get_articles(self):
        response = client.get(reverse('articles-list'))
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_article(self):
        response = client.get(reverse('articles-detail', kwargs={'pk': self.first_article.pk}))
        serializer = ArticleSerializer(self.first_article, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_article(self):
        response = client.delete(reverse('articles-detail',
                                         kwargs={'pk': self.first_article.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('articles-detail', kwargs={'pk': self.first_article.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_article(self):
        valid_article = {
            'title': 'Третья статья',
            'places': [self.izhad.pk],
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk],
            'content': 'Текст третьей статьи',
            'events': [self.new_year.pk, self.christmas.pk]
        }
        response = client.post(reverse('articles-list'),
                               data=json.dumps(valid_article, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Article.objects.get(title='Третья статья')
                         .artists.get(name='Герард Дау').pk, self.dau.pk)

    def test_create_invalid_article(self):
        invalid_article = {
            'name': 'Третья статья',
            'places': [self.izhad.pk],
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk],
            'content': 'Текст третьей статьи',
            'events': [self.new_year.pk, self.christmas.pk]
        }
        response = client.post(reverse('articles-list'),
                               data=json.dumps(invalid_article, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_article(self):
        valid_article = {
            'title': 'Новая первая статья',
            'places': [self.izhad.pk],
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk],
            'content': 'Новый текст первой статьи',
        }
        response = client.put(reverse('articles-detail', kwargs={'pk': self.first_article.pk}),
                              data=json.dumps(valid_article, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Article.objects.get(pk=self.first_article.pk).title, 'Новая первая статья')

    def test_invalid_update_article(self):
        invalid_article = {
            'name': 'Новая первая статья',
            'places': [self.izhad.pk],
            'paintings': [self.allegory_of_music.pk, self.hermit.pk],
            'artists': [self.rembrandt.pk, self.dau.pk],
            'content': 'Новый текст первой статьи',
            'events': [self.new_year.pk, self.christmas.pk]
        }
        response = client.put(reverse('articles-detail', kwargs={'pk': self.first_article.pk}),
                              data=json.dumps(invalid_article, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Article.objects.get(pk=self.first_article.pk).title, 'Первая статья')


class ApiCommentTest(TestCase):
    def setUp(self):
        self.rembrandt = Artist.objects.create(name='Рембрандт Харменс ван Рейн',
                                               is_master=True,
                                               artist_date=datetime.date(1606, 7, 15))
        self.dau = Artist.objects.create(name='Герард Дау',
                                         is_master=False,
                                         artist_date=datetime.date(1613, 4, 7))
        self.landscape = Genre.objects.create(genre_name='Пейзаж')
        self.still_live = Genre.objects.create(genre_name='Натюрморт')
        self.allegory_of_music \
            = Painting.objects.create(title='Аллегория музыки',
                                      author=self.rembrandt,
                                      painting_date=0)
        self.allegory_of_music.genres.add(self.landscape.pk, self.still_live.pk)
        self.allegory_of_music.save()
        self.hermit = Painting.objects.create(title='Отшельник',
                                              author=self.dau,
                                              painting_date=0)
        self.hermit.genres.add(self.still_live.pk)
        self.hermit.save()
        self.izhad = Place.objects.create(name="Ижад")
        self.miras = Place.objects.create(name="Мирас")
        self.new_year = Event.objects.create(name='Новый год',
                                             place=self.izhad)
        self.christmas = Event.objects.create(name='Рождество',
                                              place=self.miras)
        self.first_article = Article.objects.create(title='Первая статья',
                                                    content='Текст первой статьи')
        self.first_article.places.add(self.izhad.pk, self.miras.pk)
        self.first_article.artists.add(self.rembrandt.pk, self.dau.pk)
        self.second_article = Article.objects.create(title='Вторая статья',
                                                     content='Текст второй статьи')
        self.second_article.paintings.add(self.allegory_of_music.pk, self.hermit.pk)
        self.second_article.events.add(self.new_year.pk, self.christmas.pk)
        self.comment1 = Comment.objects.create(article=self.second_article,
                                               content='Текст комментария 1')
        self.comment2 = Comment.objects.create(article=self.second_article,
                                               parent=self.comment1,
                                               content='Текст комментария 2')

    def test_get_comments(self):
        response = client.get(reverse('comments-list'))
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_comment(self):
        response = client.get(reverse('comments-detail', kwargs={'pk': self.comment2.pk}))
        serializer = CommentSerializer(self.comment2, many=False)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        response = client.delete(reverse('comments-detail',
                                         kwargs={'pk': self.comment2.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('comments-detail', kwargs={'pk': self.comment2.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        response = client.get(reverse('comments-detail', kwargs={'pk': self.comment1.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_child_comment(self):
        response = client.delete(reverse('comments-detail',
                                         kwargs={'pk': self.comment1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = client.get(reverse('comments-detail', kwargs={'pk': self.comment1.pk}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_create_valid_comment(self):
        valid_comment = {
            'article': self.second_article.pk,
            'parent': self.comment2.pk,
            'content': 'Текст третьего комментария'
        }
        response = client.post(reverse('comments-list'),
                               data=json.dumps(valid_comment, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.get(content='Текст третьего комментария').parent.pk,
                         self.comment2.pk)

    def test_create_invalid_comment(self):
        invalid_comment = {
            'article_name': self.second_article.pk,
            'parent': self.comment2.pk,
            'content': 'Текст третьего комментария'
        }
        response = client.post(reverse('comments-list'),
                               data=json.dumps(invalid_comment, cls=DjangoJSONEncoder),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_valid_update_comment(self):
        valid_comment = {
            'article': self.second_article.pk,
            'content': 'Измененный текст второго комментария',
            'parent': ''
        }
        response = client.put(reverse('comments-detail', kwargs={'pk': self.comment2.pk}),
                              data=json.dumps(valid_comment, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Comment.objects.get(pk=self.comment2.pk).content,
                         'Измененный текст второго комментария')
        self.assertEqual(Comment.objects.get(pk=self.comment2.pk).parent, None)

    def test_invalid_update_event(self):
        invalid_comment = {
            'article_name': self.second_article.pk,
            'content': 'Измененный текст второго комментария'
        }
        response = client.put(reverse('comments-detail', kwargs={'pk': self.comment2.pk}),
                              data=json.dumps(invalid_comment, cls=DjangoJSONEncoder),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Comment.objects.get(pk=self.comment2.pk).content, 'Текст комментария 2')
        self.assertEqual(Comment.objects.get(pk=self.comment2.pk).parent.pk, self.comment1.pk)
