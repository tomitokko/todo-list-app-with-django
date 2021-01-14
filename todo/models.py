from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self):
        return self.title