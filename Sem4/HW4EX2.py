# В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке,
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод
# — на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

def max_prod(bed_params):
    tmp_max_prod = sum(prod_list[0:3])
    #Создадим новый список, дополнив исходный.В начало поставимь последний элемент
    #исходного, а в конец нулевой элемент исходного списка
    new_params = bed_params.copy()
    new_params.insert(0,bed_params[len(bed_params)-1])
    new_params.append(bed_params[0])

    #посчитаем суммы трех последовательных элементов в диапазоне индексов
    #от первого до предпоследнего, таким образом центральные элементы троек покроют исходный список
    for i in range(1,len(new_params)-1):
        tmp_sum = sum(new_params[(i-1):(i+2)])
        if tmp_sum > tmp_max_prod:
            tmp_max_prod = tmp_sum

    return tmp_max_prod

# Входной параметр грядки:
prod_list = [5,1,2,3,4]

print('максимальный урожай: ',max_prod(prod_list))
