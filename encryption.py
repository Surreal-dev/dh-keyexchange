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

def cleantext(message):

    message = ''.join(c for c in message if c.isalnum())

    message = message.lower()

    message = ''.join(message)
    return message

def encrypt(message, key):
     
    encrypted = ''
    
    uni1 = []
    uni2 = []

    bin1 = []
    bin2 = []


    for char1, char2 in zip(message, key):

        uni1.append(str(ord(char1)))
        uni2.append(str(ord(char2)))

    for uni, code in zip(uni1, uni2):

        

        bin1.append()


        

p = generatePrime()
g = primitiveRoot(p)

a = random.randint(1, p-1)

A = (g ** a) % p 

b = random.randint(1, p-1)

B = (g ** b) % p 

AliceS = (B ** a) % p 

BobS = (A ** b) % p 

SS = AliceS

if __name__ == "__main__":

    message = input("Enter a message to encrypt: ")
    cleantext(message)


