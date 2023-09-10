# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

n = int(input('Введите количество элементов первого множества: '))
m = int(input('Введите количество элементов второго множества: '))

def set_input(N):
    numbers = set()
    for i in range(N):
        numbers.add(int(input('Введите элемент N'+str(i)+': ')))

    return numbers

print('Ввод первого множества')
set_1 = set_input(n)
print('Ввод второго множества')
set_2 = set_input(m)

print('Set 1:\n', *set_1)
print('Set 2:\n', *set_2)

final_list = list(set_1.intersection(set_2))
final_list.sort()

print('Result: ', *final_list)