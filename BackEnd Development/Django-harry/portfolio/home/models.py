from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=25)
    email = models.EmailField(max_length=30)
    phone = models.IntegerField(max_length=12)
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email