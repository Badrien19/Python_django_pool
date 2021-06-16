# -*- coding: utf-8 -*-

def file_converter():
    with open('numbers.txt', 'r') as file:
        data = file.read()
    list_data = data.replace('\n', '')
    list_data = list_data.split(',')
    for nb in list_data:
        print(nb)
if __name__ == '__main__':
    file_converter()