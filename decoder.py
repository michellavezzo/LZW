import struct

# open the binary file in read mode
with open('binary_data.bin', 'rb') as file:
    # read the binary data from the file
    binary_data = file.read()

# unpack the binary data into an array of integers
int_array = list(struct.unpack('>' + 'i'*(len(binary_data)//4), binary_data))

# print the array of integers
print(int_array)