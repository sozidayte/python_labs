def summa_chisel(spisok_strok):
    total = 0
    for i in spisok_strok:
        try:
            number = float(i)
            total += number
        except ValueError:
            print(f"Невозможно преобразовать '{i}' в число!")
            continue
    return total
    
spisok_strok = ["1", "26", "77.7", "-9.99", "Evtushenko", "5"]
result = summa_chisel(spisok_strok)
print(result)
