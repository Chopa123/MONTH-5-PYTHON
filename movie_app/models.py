from django.db import models


class Director(models.Model):
    name = models.CharField(max_length=80)

    def __str__(self):
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    director = models.ForeignKey(Director, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.title

    @property
    def movie_name(self):
        try:
            return self.movie.name
        except:
            return None


@property
def filtered_reviews(self):
    return Review.objects.all(prduct_id=self.id)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE,
                              related_name='reviews')

    text = models.TextField()
    movie = models.TextField
    stars = models.IntegerField(
        choices=(
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4),
            (5, 5),
        )
    )

    def __str__(self):
        return self.text.title()
