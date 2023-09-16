# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import random

items = {
    'палатка': 7,
    'спальник': 4,
    'фонарик': 1,
    'еда': 5,
    'вода': 3,
}
max_weight = 10
current_weight = 0
packed_items = []

item_list = list(items.items())

while item_list:
    random_item = random.choice(item_list)
    item_name, item_weight = random_item

    if current_weight + item_weight <= max_weight:
        packed_items.append(random_item)
        current_weight += item_weight

    item_list.remove(random_item)


print(f'\nМаксимальная грузоподъемность рюкзака: {max_weight}\n')
print("Вещи, которые можно положить в рюкзак:")

for item in packed_items:
    print(f"{item[0]} (масса: {item[1]})")
print(f'\nИтоговый вес: {current_weight}')