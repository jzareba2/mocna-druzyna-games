from django.db import models
from django.contrib.auth.models import User


"The Player Character. Relation: One-to-One with User. "

class Hero(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    hp = models.IntegerField(default=100)
    max_hp = models.IntegerField(default=100)
    xp = models.IntegerField(default=0)
    level = models.IntegerField(default=1)
    x_pos = models.IntegerField(default=0)
    y_pos = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} (Lvl {self.level})"
    
