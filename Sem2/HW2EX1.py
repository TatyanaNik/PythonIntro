#На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

coinList = [0,1,0,0,1,1,1,0,1]
#воспользуемся тем, что сумма списка, состоящего только из 0 и 1, равна количеству единиц в списке
res = sum(coinList) if sum(coinList) <= len(coinList)//2 else len(coinList) - sum(coinList)

print(res)