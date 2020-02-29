from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    date_add = models.DateTimeField(default=timezone.now)
    cover = models.ImageField(upload_to='covers')
    file = models.FileField(upload_to='files')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('book-detail', kwargs={'pk': self.pk})
