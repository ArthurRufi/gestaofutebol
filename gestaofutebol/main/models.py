from django.db import models

class Players(models.Model):
    playername = models.CharField(max_length = 40)
    playerage = models.DateField()
    imagem = models.IntegerField(null = True)
    funcao = models.IntegerField(null = True)
    
    def __str__(self):
        return self.playername