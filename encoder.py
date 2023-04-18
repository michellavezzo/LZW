import sys
import array

from sys import argv
from struct import *

input_file = argv[1]

file = open(input_file)
data = file.read()

k = input('Digite o valor de K: ')

maximum_table_size = pow(2,int(k))

dictionary_size = 256
dictionary = {chr(i): i for i in range(dictionary_size)}
string = ""
compressed_data = []

for symbol in data:
    string_plus_symbol = string + symbol
    if string_plus_symbol in dictionary:
        string = string_plus_symbol
    else:
        compressed_data.append(dictionary[string])
        if(len(dictionary) <= maximum_table_size):
            dictionary[string_plus_symbol] = dictionary_size
            dictionary_size += 1
        string = symbol

if string in dictionary:
    compressed_data.append(dictionary[string])

# TODO: write the bin file
print(compressed_data)

## ??????
# Cria um array de inteiros
my_array = array.array('i', compressed_data)

# Abre o arquivo em modo de escrita binária
with open('arquivo.bin', 'wb') as f:
    # Escreve o array no arquivo
    my_array.tofile(f)

file.close()