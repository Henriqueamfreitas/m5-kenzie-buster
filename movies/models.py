from django.db import models

# Create your models here.
class Movie(models.Model):                                                             
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, default='', blank=True)
    RATING_CHOICES = [
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', 'NC-17'),
    ]
    rating = models.CharField(max_length=20, choices=RATING_CHOICES, default='G')
    synopsis = models.TextField(default='', blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="movies", null=True
    )
    