from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        date_posted = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        price = models.IntegerField()
        weight = models.IntegerField()
        image = models.ImageField(default='default-package.jpg', upload_to='post_image')

        def __str__(self):
            return self.title

        def get_absolute_url(self):
            return reverse('post-detail', kwargs={'pk': self.pk})

class Application(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    application_date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField()

    def __str__(self):
        return self.post.title
