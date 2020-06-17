from django.db import models


class Calendar(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    date_time = models.DateTimeField(unique=True)




