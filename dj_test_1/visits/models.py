from django.db import models


class Visits(models.Model):
    count = models.IntegerField(default=0)
