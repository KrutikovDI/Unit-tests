from main import channel_max_sales, number_requests, unique_geo_id

import pytest

class TestChannelMaxSales:
    @pytest.mark.parametrize(
        "stats, expected_sales", [
        ({'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}, 'Канал с максимальным объемом продаж: yandex'),
        ({'mail': 59, 'utube': 320, 'IPTV': 85}, 'Канал с максимальным объемом продаж: utube')
        ]
    )
    
    def test_channel_max_sales(self, stats, expected_sales):
        result = channel_max_sales(stats)
        assert result == expected_sales
    
class TestNumberRequests:
    @pytest.mark.parametrize(
        "queries, expected_number", [
        (['смотреть сериалы онлайн', 'новости спорта', 'афиша кино', 'курс доллара', 'сериалы этим летом', 'курс по питону', 'сериалы про спорт'], 'Запросов из одного слова 0%\nЗапросов из двух слов 43%\nЗапросов из трех слов 57%\nЗапросов из четырех слов 0%'),
        (['погода в Москве', 'новости', 'дешевые билеты на самолет', 'курс доллара сегодня', 'рецепт', 'популярные маркетплейсы', 'поездка в отпуск'], 'Запросов из одного слова 29%\nЗапросов из двух слов 14%\nЗапросов из трех слов 43%\nЗапросов из четырех слов 14%')
        ]
    )   
    def test_number_requests(self, queries, expected_number):
        result = number_requests(queries)
        assert result == expected_number

from unittest import TestCase

class TestUnique(TestCase):
    def test_unique_geo_id_1(self):
        ids1 = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}
        excepted_id = {98, 35, 15, 213, 54, 119}
        result = unique_geo_id(ids1)
        self.assertEqual(result, excepted_id)
        self.assertSetEqual(result, excepted_id)

    def test_unique_geo_id_2(self):
        ids1 = {'user1': [213, 213, 213, 15, 213],
        'user2': [15, 54, 119, 119, 119],
        'user3': [213, 98, 98, 54]}
        excepted_id = {98, 15, 213, 54, 119}
        result = unique_geo_id(ids1)
        self.assertEqual(result, excepted_id)