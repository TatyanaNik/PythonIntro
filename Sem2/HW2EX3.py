# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import math

N = 50
pow2List = [2**n for n in range(int(math.log2(N))+1)]
print(pow2List)

