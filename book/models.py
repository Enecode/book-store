from django.db import models


# Create your models here.
class Book(models.Model):
    GENRE_CHOICE = (
        ("C", "Comedy"),
        ("T", "Tragedy"),
        ("TC", "Tragicomedy"),
        ("CR", "Crime"),
        ("R", "Romance"),
        ("SF", "Science Fiction"),

    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(db_index=True, default="-")
    isbn = models.CharField(max_length=120)
    date_published = models.DateField()
    date_added = models.DateField(auto_now=True)
    edition = models.PositiveSmallIntegerField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICE, default="R")
