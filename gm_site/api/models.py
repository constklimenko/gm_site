from django.db import models


class Artist(models.Model):
    """Класс Художник. Содержит информацию для профиля."""
    is_master = models.BooleanField(default=False)
    name = models.CharField(max_length=250, unique=True)
    photo = models.ImageField(upload_to="", verbose_name="Фото",
                              null=True, blank=True)
    artist_date = models.DateField(auto_now=False,
                                   null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Художник"
        verbose_name_plural = "Художники"


class Genre(models.Model):
    """Класс Жанр."""
    genre_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.genre_name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Painting(models.Model):
    """Класс Картина. Содержит первичный ключ для формирования персональных
    галерей художников и просмотра отдельных картин.
    Содержит связь 'Многие ко многим' с жанрами."""
    title = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="", verbose_name="Фото",
                              null=True, blank=True, unique=False)
    author = models.ForeignKey(Artist, on_delete=models.SET_NULL,
                               null=True, blank=True)
    genres = models.ManyToManyField(Genre, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    painting_date = models.PositiveSmallIntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Картина"
        verbose_name_plural = "Картины"


class Gallery(models.Model):
    """Класс-галерея для тематической агрегации картин"""
    name = models.CharField(max_length=250)
    paintings = models.ManyToManyField(Painting, blank=True)


class Place(models.Model):
    """Класс Площадка. Означает площадку проведения выставок и прочих Event-ов."""
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="", verbose_name="Фото",
                              null=True, blank=True, unique=False)
    address = models.CharField(max_length=250,
                               null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)  # Широта.
    longitude = models.FloatField(null=True, blank=True)  # Долгота.

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Площадка"
        verbose_name_plural = "Площадки"


class Event(models.Model):
    """Класс Событие. Имеет привязку к Площадке, Художникам, Картинам."""
    name = models.CharField(max_length=250)
    photo = models.ImageField(upload_to="", verbose_name="Фото",
                              null=True, blank=True, unique=False)
    place = models.ForeignKey(Place, on_delete=models.SET_NULL,
                              null=True, blank=True)
    paintings = models.ManyToManyField(Painting, blank=True)
    artists = models.ManyToManyField(Artist, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    event_date = models.DateField(auto_now=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Событие"
        verbose_name_plural = "События"


class Article(models.Model):
    """Класс Статья. Может иметь привязку к Событиям, Площадкам, Художникам, Картинам.
    TODO: подключить движок тегов."""
    for_main = models.BooleanField(default=False)  # Статья не для блога, а для главной страницы.
    title = models.CharField(max_length=250)
    places = models.ManyToManyField(Place, blank=True)
    paintings = models.ManyToManyField(Painting, blank=True)
    artists = models.ManyToManyField(Artist, blank=True)
    events = models.ManyToManyField(Event, blank=True)
    datetime = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"


class Comment(models.Model):
    """Класс Комментарий. Привязывается к статье и к родительскому комментарию, если есть.
    TODO: Переработать с учетом аутентификации через соцсети."""
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                null=False, blank=False)
    parent = models.ForeignKey('self', on_delete=models.SET_NULL,
                               blank=True, null=True, related_name='child_set')
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.article.name} - комментарий №{self.pk}"

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
