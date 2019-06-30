from django.db import models


class Chat(models.Model):
    content1 = models.TextField()
    content2 = models.TextField()
