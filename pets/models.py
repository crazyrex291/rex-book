from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self) -> str:
        return self.name
