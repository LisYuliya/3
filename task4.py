# Задание с семинара

# Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции с множествами. Код должен расширяться на любое большее количество друзей.

friends_items = {
    'Никита': {'спальник', 'фонарик', 'еда'},
    'Артур': {'палатка', 'спальник', 'еда', 'вода', 'карта', 'фонарик'},
    'Николай': {'палатка','еда', 'спальник'},
}

friends_items = {
    'Никита': {'спальник','какао', 'фонарик', 'еда'},
    'Артур': {'палатка', 'спальник', 'еда', 'вода', 'карта'},
    'Николай': {'палатка','еда', 'спальник', 'спички', 'фонарик'},
}

intersection_all = set.intersection(*friends_items.values())

unique_items = set()
item_counts = {}
for items in friends_items.values():
    for item in items:
        if item in item_counts:
            item_counts[item] += 1
        else:
            item_counts[item] = 1

for item, count in item_counts.items():
    if count == 1:
        unique_items.add(item)

common_except_one = {}
for friend1 in friends_items:
    items1 = friends_items[friend1]
    others = {friend2: items2 for friend2, items2 in friends_items.items() if friend2 != friend1}
    common_items = set.intersection(*others.values())

    for item in common_items:
        if item not in items1:
            common_except_one[item] = friend1

print(f'\nВещи, которые взяли все друзья: {intersection_all} \n')
print(f'Уникальные вещи, есть только у одного друга:, {unique_items} \n')
print(f'Вещи, которые есть у всех друзей кроме одного: ')
for item, friend in common_except_one.items():
    print(f"{item} (отсутствует у {friend})")