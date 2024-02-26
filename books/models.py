from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    summary = models.TextField(default="Your default summary here")
    cover_image = models.ImageField(upload_to="book/images/", null=True, blank=True)

    def __str__(self):
        return self.title
