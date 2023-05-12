
def channel_max_sales(stats):
    stats_list = list(stats)
    max_values = 0
    id_values = -1
    for values in stats.values():
        if values > max_values:
            max_values = values
            id_values += 1
    return f'Канал с максимальным объемом продаж: {stats_list[id_values]}'


def number_requests(queries):
    num_queries = len (queries)
    guaries1 = 0
    guaries2 = 0
    guaries3 = 0
    guaries4 = 0
    for query in queries:
        query_list = query.split(' ')
        world_query = len(query_list)
        if world_query == 1:
            guaries1 += 1
        elif world_query == 2:
            guaries2 += 1
        elif world_query == 3:
            guaries3 += 1
        elif world_query == 4:
            guaries4 += 1
    return f'Запросов из одного слова {round(guaries1 * 100 / num_queries)}%\nЗапросов из двух слов {round(guaries2 * 100 / num_queries)}%\nЗапросов из трех слов {round(guaries3 * 100 / num_queries)}%\nЗапросов из четырех слов {round(guaries4 * 100 / num_queries)}%'


def unique_geo_id(ids):
    return set(sum(ids.values(), []))

if __name__ == '__main__':
    # stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
    # result = channel_max_sales(stats)
    # print(result)

    # queries = [
    # 'погода в Москве', 'новости', 'дешевые билеты на самолет', 'курс доллара сегодня', 'рецепт', 'популярные маркетплейсы', 'поездка в отпуск'
    # ]
    # result = number_requests(queries)
    # print(result)

    ids = {'user1': [213, 213, 213, 15, 213],
        'user2': [54, 54, 119, 119, 119],
        'user3': [213, 98, 98, 35]}
    result = unique_geo_id(ids)
    print((result))