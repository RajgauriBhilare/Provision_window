from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description = models.TextField()
    image = models.URLField(blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ContactEnquiry(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=50)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'
