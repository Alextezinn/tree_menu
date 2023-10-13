"""
Модуль моделей приложения
"""
from django.db import models
from django.urls import reverse


class Menu(models.Model):
    """
    Класс меню
    """
    title = models.CharField(max_length=255, unique=True, verbose_name='Название меню')
    slug = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name="Slug меню")

    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'


class MenuItem(models.Model):
    """
    Класс элементов меню
    """
    title = models.CharField(max_length=255, verbose_name='Название элемента меню')
    slug = models.SlugField(max_length=255, db_index=True, unique=True,
                            verbose_name="Slug элемента меню")
    parent = models.ForeignKey('self', blank=True, null=True,
                               related_name='childrens', on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, blank=True, related_name='items', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('item', kwargs={'item_slug': self.slug})

    class Meta:
        verbose_name = 'Элемент меню'
        verbose_name_plural = 'Элемент меню'
