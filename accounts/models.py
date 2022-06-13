from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.urls import reverse


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)
    address = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to='photo', null=True, blank=True)


class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories'

    def get_url(self):
        return reverse('blog_cat', args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)


class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='blog', null=True, blank=True)
    summary = models.TextField()
    content = models.TextField()
    categ = models.ForeignKey(Category, on_delete=models.CASCADE)
    draft = models.BooleanField(default=False)

    def __str__(self):
        return self.title
