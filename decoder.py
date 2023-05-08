import struct


k = input('Digite o valor de K: ')
maximum_table_size = pow(2, int(k))

dictionary_size = 256

dictionary =  {i: chr(i) for i in range(dictionary_size)}
decompressed_data = ""
string = ""
decoded = ""
next_code = 256
# file_type = 'txt' # line40 - duplicated to be easy to debug

# open the binary file in read mode
with open('binary_data.bin', 'rb') as file:
    # read the binary data from the file
    binary_data = file.read()

# unpack the binary data into an array of integers
int_array = list(struct.unpack('>' + 'i'*(len(binary_data)//4), binary_data))

for i, code in enumerate(int_array):
    if i == 0:
        string = dictionary[code] 
        decoded = decoded+string
    else:
        if (code not in dictionary): 
            new_string = string + (string[0])
        else:
            new_string = dictionary[code]
        decoded += new_string
        if (len(dictionary) <= maximum_table_size):
            dictionary[next_code] = string + (new_string[0])
            next_code += 1
        string = new_string

file_type = 'mp4' ## duplicated to be easy to debug
## choose the write type based on the file type
if (file_type == 'txt'):
    writeType = 'w' 
else:
    writeType = 'wb'
# create a file to write the decompressed data
# 
with open('decompressed_data.' + file_type, writeType) as file:  
    # write the decompressed data to the file
    if (file_type == 'txt'):
        file.write(decoded.encode('latin-1').decode('utf-8'))
    else:
        # Write media file
        file.write(bytearray(decoded.encode('latin-1')))