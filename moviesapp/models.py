from django.db import models

# Create your models here.


class SearchTerm(models.Model):
    term = models.TextField(unique=True)
    last_search = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.term

    class Meta:
        ordering = ["id"]
        db_table = "search_terms"


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        db_table = "genres"


class Movie(models.Model):
    genres = models.ManyToManyField(Genre, related_name="movies")
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    runtime_minutes = models.PositiveIntegerField(null=True)
    imdb_id = models.SlugField(unique=True)
    plot = models.TextField(null=True, blank=True)
    is_full_record = models.BooleanField(default=False)

    class Meta:
        ordering = ["title", "year"]
        db_table = "movies"