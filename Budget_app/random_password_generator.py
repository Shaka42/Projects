import random
import string

a = string.ascii_letters+string.ascii_letters+string.punctuation
inp = int(input('Enter length of password:'))
def generator(inp):
    c =[]
    for i in range(inp):
        b = random.choice(a)
        c.append(b)
    password = ''.join(c)
    print('passoword generated:',password)
    
generator(inp)
        