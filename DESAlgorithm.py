# DES Algorithm
import random
message_len = 64
half_message_len = 32
string_len = 48
character_len = 8
rounds = 16
key_len = 56
sbox1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], 
		 [0, 15, 7, 4, 14,2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], 
		 [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], 
		 [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

sbox2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		 [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		 [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		 [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

sbox3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		 [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		 [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		 [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

sbox4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		 [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		 [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		 [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

sbox5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		 [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		 [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		 [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

sbox6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		 [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		 [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		 [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

sbox7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		 [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		 [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		 [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

sbox8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		 [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		 [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		 [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]

straight_permutation = [16, 7, 20, 21, 29, 12, 28, 17,
						1, 15, 23, 26, 5, 18, 31, 10,
						2, 8, 24, 14, 32, 27, 3, 9,
						19, 13, 30, 6, 22, 11, 4, 25]

parity_drop_table = [57, 49, 41, 33, 25, 17, 9, 1,
					 58, 50, 42, 34, 26, 18, 10, 2,
					 59, 51, 43, 35, 27, 19, 11, 3,
					 60, 52, 44, 36, 63, 55, 47, 39,
					 31, 23, 15, 7, 62, 54, 46, 38,
					 30, 22, 14, 6, 61, 53, 45, 37,
					 29, 21, 13, 5, 28, 20, 12, 4]

compress_pbox = [14, 17, 11, 24, 1, 5, 3, 28,
					15, 6, 21, 10, 23, 19, 12, 4,
					26, 8, 16, 7, 27, 20, 13, 2,
					41, 52, 31, 37, 47, 55, 30, 40,
					51, 45, 33, 48, 44, 49, 39, 56,
					34, 53, 46, 42, 50, 36, 29, 32]

key_list = []

def binaryToDecimal(binary): 
    """
    Calculates the decimal equivalent of binary input
    """
    binary = int(binary)
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary // 10
        i += 1
    return(decimal)    

def decimalToBinary(decimal):
	"""
	Takes a Decimal input and returns a Binary string of length 4
	"""
	return('{0:04b}'.format(decimal))

def sbox(input):
	"""
	Takes 48 bits as input and returns 32 bits
	"""
	sbox = [sbox1, sbox2, sbox3, sbox4, sbox5, sbox6, sbox7, sbox8]
	output = ""
	x = 0
	k = 0
	while(x < 43):
		group = input[x : x + 6]
		row = group[0] + group[-1]
		column = group[1 : 5]
		row = binaryToDecimal(row)
		column = binaryToDecimal(column)
		value = sbox[k][row][column]
		output += decimalToBinary(value)
		k += 1
		x += 6
	return output

def expansion_pbox(input):
	"""
	Takes 32 bits string as input and returns 48 bits.
	"""
	output = ""
	x = 0
	while(x < 29):
		group = input[x : x + 4]
		index2 = (x + 4) % half_message_len
		index1 = (x - 1) % half_message_len
		if(index1 < 0):
			index1 = 31
		output += input[index1] + group + input[index2]
		x += 4
	return output

def straight_pbox(input):
	"""
	Permutes the 32 bits input binary string.
	"""
	output = ""
	for x in range(half_message_len):
		output += input[straight_permutation[x] - 1]
	return output

def xor_operation(val1, val2, k):
	output = ""
	for x in range(k):
		if(val1[x] == val2[x]):
			output += '0'
		else:
			output += '1'
	return output

def parity_drop(input):
	output = ""
	for x in range(key_len):
		output += input[parity_drop_table[x] - 1]
	return output

def compression_pbox(input):
	output = ""
	for x in range(string_len):
		output += input[compress_pbox[x] - 1]
	return output

def key_round(input, round):
	input1 = input[: key_len // 2]
	input2 = input[key_len // 2:]
	if(round == 1 or round == 2 or round == 9 or round == 16):
		input11 = input1[0]
		input1 = input1[1 :]
		input1 = input1 + input11
		input21 = input2[0]
		input2 = input2[1 :]
		input2 = input2 + input21

	else:
		input11 = input1[: 2]
		input1 = input1[2 :]
		input1 = input1 + input11
		input21 = input2[: 2]
		input2 = input2[2 :]
		input2 = input2 + input21
	key_list.append(compression_pbox(input1 + input2))
	return(input1 + input2)

def round_key_generation(input, round = 1):
	input = parity_drop(input)
	while(round < 17):
		input = key_round(input, round)
		round += 1

def des_function(right_string, key):
	"""
	Takes 32 bits binary string and key as input and returns 32 bits binary string as output.
	"""
	return straight_pbox(sbox(xor_operation(expansion_pbox(right_string), key, string_len)))

def feistel_round(input, key, round):
	"""
	Takes 64 bits as input and returns 64 bits as output.
	"""
	left_part = input[0 : half_message_len]
	right_part = input[half_message_len : message_len]
	left_part = xor_operation(left_part, des_function(right_part, key), half_message_len)
	if(round != 16):
		return right_part + left_part
	else:
		return left_part + right_part

message = input('Enter the message (max 8 characters): ')

# Encryption
padding = character_len - len(message)
message += padding * 'x'
print("Message after padding: ", message)
binary_message = ""
for x in message:
	binary_message += '{0:08b}'.format(ord(x))
print("Binary string message after padding: ", binary_message)
output = binary_message
print('Generating a random 64 bits key...')
letters = ['0', '1']
key = ''.join(random.choice(letters) for i in range(message_len))
print("Generated 64 bits key : ", key)
round_key_generation(key)
round = 1
while(round <= rounds):
	output = feistel_round(output, key_list[round - 1], round)
	round += 1
print('Encrypted 64 bits binary message: ', output)

# Decryption
round = 1
while(round <= rounds):
	output = feistel_round(output, key_list[rounds - round], round)
	round += 1
print("64 bits binary message after decryption: ", output)
x = 0
output_message = ""
while(x < (character_len - padding - 1) * character_len + 1):
	group = output[x : x + character_len]
	output_message += chr(binaryToDecimal(group))
	x += character_len
print('Decrypted message: ', output_message)

