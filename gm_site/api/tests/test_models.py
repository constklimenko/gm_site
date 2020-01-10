from django.test import TestCase

from ..models import Artist


class ArtistModelTest(TestCase):
    def setUp(self) -> None:
        Artist.objects.create(name="Иероним Босх", is_master=False)

    def test_dummy(self):
        artist = Artist.objects.get(name='Иероним Босх')
        self.assertEqual(artist.is_master, False)
