"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args) -> list:
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """

    res = []
    for i in args:
        res.append(i**2)
    return res


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num: int) -> bool:
    for i in range(1, num):
        if num == 0 or (i != 1 and i != num and num%i == 0):
            return False
    else:
        return True


def filter_numbers(nums: list, mode: str) -> list:
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if mode == ODD:
        res = list(filter(lambda num: num % 2 != 0, nums))
    elif mode == EVEN:
        res = list(filter(lambda num: num % 2 == 0 and num != 0, nums))
    elif mode == PRIME:
        res = list(filter(lambda num: is_prime(num), nums))
    else:
        res = []

    return res
