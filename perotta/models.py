from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """出品"""

    title = models.CharField('タイトル', max_length=225)
    text = models.TextField('本文', max_length=1000)
    created_at = models.DateTimeField('作成日', default=timezone.now)


    def __str__(self):
        return self.title
