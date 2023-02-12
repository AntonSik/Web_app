from django.db import models

class vote(models.Model):
    name = models.CharField('Название',max_length=100)
    full_text = models.TextField('Описание',default='Описание')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'



