# Дан список повторяющихся элементов.
# Вернуть список с повторяющимися элементами.
# В результирющем списке не должно быть дубликатов.

some_list = ['a', 'a', 'a', 'f', 'aa', 'a', 'g', 'h', 'j', 2, 3, 2, 'f']
my_list = []
for i in some_list:
    if some_list.count(i) > 1:
        if i not in my_list:
            my_list.append(i)
print(my_list)