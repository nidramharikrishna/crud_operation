from django.db import models

class student(models.Model):
    name = models.CharField(max_length=30)
    email= models.EmailField()
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.name