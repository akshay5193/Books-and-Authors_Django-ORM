from django.db import models

# Create your models here.


class Books (models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)


class Authors (models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    books = models.ManyToManyField(Books, related_name="authors")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    notes = models.CharField(
        max_length=255, default="This instance was created before altering the model!")
