from django.db import models


class Modelmassege(models.Model):
    text = models.CharField(max_length=200)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
