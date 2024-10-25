import os

def dostupen_li_file(file):
    return os.access(file, os.R_OK) and os.access(file, os.W_OK)

file = input("Введите путь к файлу: ")
if dostupen_li_file(file):
    print(f"Файл '{file}' доступен для чтения и записи.")
else:
    print(f"Файл '{file}' недоступен для чтения и записи.")
