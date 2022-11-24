from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    website = models.URLField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        reverse('book:publisher_details', args=[self.id])



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
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="+")
    author = models.ManyToManyField("Author", related_name="books")
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['title']


class Author(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.first_name


class Address(models.Model):
    number = models.PositiveIntegerField()
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=6,
                               validators=[MinLengthValidator(5, "Code cannot be less than a length of 5"),
                                           MaxLengthValidator(6, "Code can not exceed a length of 6")])
    publisher = models.OneToOneField(Publisher, on_delete=models.CASCADE)
