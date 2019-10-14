import random
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(b, n):
	ra = n
	rb = b
	ta = 0
	tb = 1
	while(rb > 0):
		q = ra // rb
		r = ra - q * rb
		ra = rb
		rb = r
		t = ta - q * tb
		ta = tb
		tb = t
	if(ra == 1):
		if(ta > 0):
			return ta
		else:
			return (ta % n)
	else:
		return(-1)

def generate_key(p, q):
	phi = (p - 1) * (q - 1)
	e = random.randint(2, phi - 1)
	g = gcd(e, phi)
	while g != 1:
	    e = random.randint(2, phi - 1)
	    g = gcd(e, phi)

	d = multiplicative_inverse(e, phi)
	return e, d

def encrypt(m, e, n):
	c = (m ** e) % n
	return c

def decrypt(c, d, n):
	p = (c ** d) % n
	return p

p = int(input("Enter a large prime number: "))
q = int(input("Enter another large prime number (Not one you entered above): "))
n = p * q
print("Generating your public/private keypairs now...")
public, private = generate_key(p, q)
print("Public key: ", public)
print("Private key: ", private)
message = int(input("Enter message: "))
print("Encrypting...")
cipher = encrypt(message, public, n)
print("Cipher text: ", cipher)
plain = decrypt(cipher, private, n)
print("Plain text after decryption: ", plain)
