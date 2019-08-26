# Diffie-Hellman Key Exchange Proptocol
n, g = map(int, input('Enter two large prime numbers: ').split())
p1 = int(input('Large random number chosen by user one: '))
p2 = int(input('Large random number chosen by user two: '))
x = int(input('Enter x chosen by user one: '))
y = int(input('Enter y chosen by user two: '))
A = (g ** x) % n
B = (g ** y) % n
print('A: ', A)
print('B: ', B)
K1 = (B ** x) % n
K2 = (A ** y) % n
print('K1: ', K1)
print('K2: ', K2)