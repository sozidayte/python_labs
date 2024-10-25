from random import random
def filter_numbers(spisok):
    return [num for num in spisok if num > 0]

input_spisok = [random() for i in range(6)]
result = filter_numbers(input_spisok)
print(result)
