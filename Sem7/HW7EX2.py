# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

def print_operation_table(operation, num_rows=6, num_columns=6):

    for row in range(1,num_rows+1):
        row_map = list(map(operation, [row]*num_columns, range(1,num_columns+1)))
        print(*row_map)

print_operation_table(lambda x, y: x * y)

