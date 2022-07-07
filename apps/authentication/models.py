from django.db import models


class User(models.Model):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    is_admin = models.BooleanField()

    def __str__(self):
        return f'User {self.username}'
