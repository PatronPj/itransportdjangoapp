from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
from PIL import Image

class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        date_posted = models.DateTimeField(default=timezone.now)
        author = models.ForeignKey(User, on_delete=models.CASCADE)
        price = models.IntegerField()
        weight = models.IntegerField()
        image = models.ImageField(default='default-package.jpg', upload_to='post_image')

        adress1 = models.CharField("Collection Address", max_length=100)
        zip_code1 = models.CharField("ZIP / Postal code",max_length=12)
        city1 = models.CharField("City",max_length=1024)

        adress2 = models.CharField("Shipping Address", max_length=100)
        zip_code2 = models.CharField("ZIP / Postal code",max_length=12)
        city2 = models.CharField("City",max_length=1024)

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
        instance = Application.objects.get(id=application)
        send_mail('Job Application', 'Your job application for: ' +instance.post.title +' was accepted. The collection adress is: '+instance.post.adress1+' in '+instance.post.zip_code1+' '+instance.post.city1+'. The shipping adress is: '+ instance.post.adress2+' in '+instance.post.zip_code2+' '+instance.post.city2+'.'
        , settings.EMAIL_HOST_USER, [instance.candidate.email], fail_silently=False)
        Application.objects.filter(id=application).update(status=2)

    @classmethod
    def decline_application(cls, application):
        instance = Application.objects.get(id=application)
        send_mail('Job Application', 'Your job application for: ' + instance.post.title +' was declined!', settings.EMAIL_HOST_USER, [instance.candidate.email], fail_silently=False)
        Application.objects.filter(id=application).update(status=3)
