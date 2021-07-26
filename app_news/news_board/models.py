from django.db import models


class NewsModel(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название новости', blank=True)
    description = models.TextField(blank=True, verbose_name='Содержание новости')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания новости')

    def __str__(self):
        return f'{self.title} ({self.created_at})'

    class Meta:
        ordering = ['created_at']
