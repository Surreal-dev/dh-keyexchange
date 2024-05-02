
import random

import math

import hashlib

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
    
    num = random.randint(10, 100000)
    
    while not isPrime(num):
        
        num = random.randint(10, 100000)
    
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


a = random.randint(1, p - 1)

A = (g ** a) % p

b = random.randint(1, p - 1)

B = (g ** b) % p

shared_secret_key_A = (B ** a) % p

shared_secret_key_B = (A ** b) % p

def encrypt(message, key):
    
    h = hashlib.sha256()
    
    h.update(str(key).encode())
    
    key = h.digest()
    print(f"key = {key}")
    
    key_length = len(key)
    
    encrypted_message = ""
    
    for i in range(0, len(message), key_length):
        
        chunk = message[i:i + key_length]
        
        for j in range(len(chunk)):
            encrypted_message += chr(ord(chunk[j]) ^ key[j])
    
    return encrypted_message

with open("message.txt", "r") as file:
    message = file.read()

encrypted_message = encrypt(message, shared_secret_key_A)

with open('encrypted.txt', 'w') as enc:
    enc.write(encrypted_message)
    enc.close()

def decrypt(encrypted_message, key):
    
    h = hashlib.sha256()
    
    h.update(str(key).encode())
    
    key = h.digest()
    
    key_length = len(key)
    
    decrypted_message = ""
    
    for i in range(0, len(encrypted_message), key_length):
        
        chunk = encrypted_message[i:i + key_length]
        
        for j in range(len(chunk)):
            decrypted_message += chr(ord(chunk[j]) ^ key[j])
    
    return decrypted_message

decrypted_message = decrypt(encrypted_message, shared_secret_key_B)

with open('decrypted.txt', 'w') as dec:
    dec.write(decrypted_message)
    dec.close()