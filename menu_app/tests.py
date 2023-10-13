"""
Модуль для тестирования
"""
import logging

from django.test import TestCase
from django.urls import reverse

from .models import Menu


logger = logging.getLogger(__name__)


class MenuTestCase(TestCase):
    """
    Класс для тестирования Django приложения
    """
    def setUp(self):
        """
        Метод установки начальных данных для работы с ними
        """
        self.menu = Menu.objects.create(
            title='test',
            slug='test'
        )
        self.menu_item1 = self.menu.items.create(
            title='item_test1',
            slug='item_test1'
        )
        self.menu_item2 = self.menu.items.create(
            title='item_test2',
            slug='item_test2'
        )
        self.menu_item3 = self.menu.items.create(
            title='item_test3',
            slug='item_test3'
        )

    def test_menu_db(self):
        self.assertEqual(Menu.objects.count(), 1)
        self.assertEqual(self.menu.items.count(), 3)
        logger.error("error")

    def test_status_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
