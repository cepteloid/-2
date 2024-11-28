from math import*
from random import *
n = int(input("Введите количество элементов массива (N <= 100): "))
if n > 100:
    n = 100
elif n < 1:
    n = 1
mas = [randint(-50, 50) for _ in range(n)]
print("\nНачальное состояние:")
for i in range(n):
    print(f"{mas[i]:7d}", end=" ")
print()
min_mod = min(abs(x) for x in mas)
sum_after_zero = 0
found_zero = False
for x in mas:
    if found_zero:
        sum_after_zero += abs(x)
    elif x == 0:
        found_zero = True

# Преобразование массива: первая половина - четные позиции, вторая - нечетные
half_n = n // 2
even_elements = mas[::2]
odd_elements = mas[1::2]
new_mas = even_elements[:half_n] + odd_elements[:half_n]

# Дополнение массива нулями, если не хватает элементов
new_mas.extend([0] * (n - len(new_mas)))

# Вывод преобразованного массива
print("\nКонечное состояние:")
for i in range(n):
    print(f"{new_mas[i]:7d}", end=" ")
print()


print(f"\nМинимальный по модулю элемент: {min_mod}")
print(f"Сумма модулей элементов после первого нуля: {sum_after_zero}")
