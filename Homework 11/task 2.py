'''
Создать функцию <fib(n)>, генерирующую <n> чисел Фибоначчи с минимальными затратами ресурсов.
'''


def fib(n: int) -> list:
    a = 1
    b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


print(list(fib(10000)))
