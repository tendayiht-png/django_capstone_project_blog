from django.db import models
from django.contrib.auth.models import User

class GameScore(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    score = models.IntegerField(default=0)
    incorrect = models.IntegerField(default=0)
    game_type = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.game_type}: {self.score}"
