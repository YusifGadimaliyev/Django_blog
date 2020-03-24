from django.db import models

# Create your models here.

class Contact(models.Model):
    email = models.EmailField()
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.email
