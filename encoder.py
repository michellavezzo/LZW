import sys
import array
import os
import struct

from sys import argv
from struct import *

# set the file path
file_path = argv[1]


## TODO: use this extension to be part of the encoded data
# get the file extension
file_extension = os.path.splitext(file_path)[1]

file = open(file_path)
data = file.read()

k = input('Digite o valor de K: ')

maximum_table_size = pow(2, int(k))

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

with open('binary_data.bin', 'wb') as file:
    # pack the integer array into binary format using the struct module
    binary_data = struct.pack('>' + 'i'*len(compressed_data), *compressed_data)
    # write the binary data to the file
    file.write(binary_data)

file.close()