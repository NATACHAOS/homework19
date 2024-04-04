def sum_range(start, end):
    if start > end:
        start, end = end, start
    s = 0
    for i in range(start, end + 1):
        s += i
    return s


a = int(input('Введите число "начало": '))
b = int(input('Введите число "конец": '))

print(('Сумма всех чисел от'), a, 'до', b, 'равна', (sum_range(a, b)))
