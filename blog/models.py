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

    @classmethod
    def apply_to_job(cls, current_user, current_post):
        Application.objects.create(post = current_post, candidate = current_user, application_date = timezone.now(), status = 1)
        current_post.application_set.all()

    @classmethod
    def delete_application(cls, application):
        instance = Application.objects.get(id=application)
        instance.delete()

    @classmethod
    def accecpt_application(cls, application):
        Application.objects.filter(id=application).update(status=2)

    @classmethod
    def decline_application(cls, application):
        Application.objects.filter(id=application).update(status=3)
