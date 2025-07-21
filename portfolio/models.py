from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class CompanyInfo(models.Model):
    name = models.CharField(max_length=200)
    motto = models.CharField(max_length=300)
    vision = models.TextField()
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    contact_name = models.CharField(max_length=100)
    contact_role = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_gender = models.CharField(max_length=20)
    contact_languages = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

class Experience(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    partners = models.CharField(max_length=300, blank=True)
    location = models.CharField(max_length=200, blank=True)
    date = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title

class Partnership(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    mou_signed = models.BooleanField(default=False)
    is_functional = models.BooleanField(default=True)

    def __str__(self):
        return self.name
