import struct



k = input('Digite o valor de K: ')
maximum_table_size = pow(2, int(k))

dictionary_size = 256

dictionary =  {i: chr(i) for i in range(dictionary_size)} #{chr(i): i for i in range(dictionary_size)}
decompressed_data = ""
string = ""
decoded = ""
next_code = 256
file_type = ''


# open the binary file in read mode
with open('binary_data.bin', 'rb') as file:
    # read the binary data from the file
    binary_data = file.read()

# unpack the binary data into an array of integers
int_array = list(struct.unpack('>' + 'i'*(len(binary_data)//4), binary_data))

# print(int_array)

# lzw decompress algorithm
# for code in int_array:
#     if not (code in dictionary):
#         dictionary[code] = string + (string[0])    
#         # print(dictionary[code])
#     decompressed_data += dictionary[code]
#     if (len(string) == 0):
#         dictionary[next_code] = string + (dictionary[code][0])
#         next_code += 1
#     string = dictionary[code]


for i, code in enumerate(int_array):
    if i == 0:
        string = dictionary[code] 
        decoded = decoded+string
    else:
        if (code not in dictionary):
            # dictionary[code] = string + (string[0])    
            new_string = string + (string[0])
        else:
            new_string = dictionary[code]
            # print(dictionary[code])
        decoded += new_string
        if (len(dictionary) <= maximum_table_size):
            dictionary[next_code] = string + (new_string[0])
            next_code += 1
        string = new_string


# create a file to write the decompressed data
with open('decompressed_data.mp4', 'wb') as file:
    
    # write the decompressed data to the file
    if (file_type == 'txt'):
        file.write(decoded.encode('latin-1').decode('utf-8'))
    else:
        #  file.write mp4 file
        file.write(bytearray(decoded.encode('latin-1')))




# print the array of integers
# print(int_array)