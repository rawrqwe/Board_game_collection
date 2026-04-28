from django.db import models

class BoardGame(models.Model):
    title = models.CharField(max_length=200),
    min_players = models.PositiveIntegerField(default=1),
    max_players = models.PositiveIntegerField(default=4),
    play_time = models.CharField(max_length=20, verbose_name="Czas gry (np. 30-60 min)"),
    category = models.CharField(max_length=100),
    description = models.CharField(max_length=1000),

    #Na późniejszym etapie
    # Photo_box = models.IntegerField()