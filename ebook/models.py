from django.db import models
from store.models import Category
from django.contrib.auth.models import User

# Create your models here.
class Ebook(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="ebook/")
    categories = models.ManyToManyField(Category, related_name='ebooks')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ebooks')
    summary = models.TextField(blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.id} - {self.name}"


class Chapter(models.Model):
    ebook = models.ForeignKey(Ebook, related_name='chapters', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    order = models.PositiveIntegerField(unique=True)  # To maintain chapter sequence

    class Meta:
        ordering = ['order']  # Ensures chapters are retrieved in order

    def __str__(self):
        return f"{self.ebook.name} - {self.title}"
