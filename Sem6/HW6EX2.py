# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
import random

left_num = random.randint(-10, 10)

right_num = random.randint(left_num+1, left_num+1+random.randint(10, 20))

test_list = [random.randint(left_num-10, right_num+10) for _ in range(0, random.randint(10, 20))]

result_list = [i for i in range(0, len(test_list)) if left_num <= test_list[i] <= right_num]

print(left_num,right_num)
print(test_list)
print(result_list)
