from django.db import models

# Create your models here.
class Info(models.Model):
    name=models.CharField(max_length=20)
    birth=models.IntegerField(default=00000000)
    nickname=models.CharField(max_length=20)
    introduce=models.CharField(max_length=50)

    def __str__(self):
        return f'{self.pk}. {self.name}'
