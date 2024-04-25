import pandas as pd 
import random
import math


def isPrime(number):

    if number == 2:
        
        return True
    
    if number % 2 == 0:
        
        return False
    
    sqrt = math.sqrt(number)
    
    sqrt = int(sqrt)
    
    for i in range(3, sqrt + 1, 2):
        
        if number % i == 0:
            
            return False
    
    return True

def generatePrime():
    
    num = random.randint(2, 1000)
    
    while not isPrime(num):
        
        num = random.randint(2, 1000)
    
    return num

def primitiveRoot(prime):
    
    for i in range(2, prime):
        
        powers = []
        
        for j in range(1, prime):
            
            power = (i ** j) % prime
            
            if power in powers:
                
                break
            
            powers.append(power)
        
        if len(powers) == prime - 1:
            
            return i
    
    return None

p = generatePrime()
g = primitiveRoot(p)

a = random.randint(1, p-1)

A = (g ** a) % p 

b = random.randint(1, p-1)

B = (g ** b) % p 

AliceS = (B ** a) % p 

BobS = (A ** b) % p 

df = pd.DataFrame({
    "Alice": [g, p, A, B, AliceS]
    "Eve": [g, p, A, B]
    "Bob": [g, p, A, B, BobS]
})

df.style \
  .format(precision=3, thousands=".", decimal=",") \
  .format_index(str.upper, axis=1) \

print(df) 