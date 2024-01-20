from django.db import models

class Players():
    playername : models.CharField(max_length = 40)
    playerage : models.DateField()
