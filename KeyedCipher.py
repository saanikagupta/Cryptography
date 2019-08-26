import math
import random

def encrypt(plain, size, key):
	cipher_groups = []
	groups = []
	bogus = len(plain) % size
	if(bogus != 0):
		bogus = size - bogus
	plain = plain + bogus * 'z'
	for x in range(0, len(plain), size):
		groups.append(plain[x : x + size])

	for x in groups:
		s = ''
		for y in range(size):
			s += x[key[y]]
		cipher_groups.append(s)
	cipher =  " ".join(cipher_groups)
	return (cipher, bogus)

def decrypt(cipher, size, key, bogus):
	groups = []
	plain_groups = []
	i = 0
	for x in range(0, len(cipher) - 1, size):
		groups.append(cipher[x + i : x  + i + size])
		i += 1
	for x in groups:
		s = ''
		for y in range(size):
			ind = key.index(y)
			s += x[ind]
		plain_groups.append(s)
	plain = "".join(plain_groups)
	plain = plain[: -bogus]
	return plain

plain = input('Enter the plain text: ')
group_size = int(input('Enter the group size: '))
range_plain = math.ceil(len(plain) / group_size)
key = list(range(group_size))
random.shuffle(key)
cipher, bogus = encrypt(plain, group_size, key)
print("Key : ", key)
print('After encryption: ', cipher)
plain = decrypt(cipher, group_size, key, bogus)
print('After decryption: ', plain)
