from django.conf import settings
from django.db import models
from django.utils import timezone


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Автор')
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст')
    created_date = models.DateTimeField(default=timezone.now, verbose_name='дата создания')
    published_date = models.DateTimeField(blank=True, null=True, verbose_name='дата публикации')


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

    
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    
    def __str__(self):
        return self.title