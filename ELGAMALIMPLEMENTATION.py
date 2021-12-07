#!/usr/bin/env python
# coding: utf-8

# In[4]:


import random
import sys

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modularInverse(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m
    
def getpublickey():

    p_input = input("Enter the prime number p between 1k and 100k:")
    p = int( p_input)
    if p > 1:
        for i in range(2, p//2):
            if (p % i) == 0:
                print(p, "is not a prime number")
                sys.exit()
                break       
    d = random.randint(1, p-2)   #Private Key
    e1 = random.randint(1, p-1)  #Public Key
    e2 = pow(e1,d,p)
    
    return p, d, e1, e2


def Encryption(message, p, e1, e2): 
  
    encryptedmessage = ""
    r = random.randint(1,p-1) 
    c1 = pow(e1,r,p)
    
    for i in message: 
        m=ord(i)
        encryptedmessage+=str((pow(e2,r) * m)%p)+" "  #ascii 
        

    print("A Public Key  (c1):",c1)
    print("A Private Key (r):",r)
    print("Encrypted Message :", encryptedmessage);
    return encryptedmessage, c1


def Decryption(encryptedmessage, p, d, e1, c1): 
  
    decryptedmessage = "" 
    parts=encryptedmessage.split()
    for part in parts:
        if part:
            c=int(part)
            decryptedmessage+=chr((c *modularInverse(pow(c1,d,p),p)) % p)

    return decryptedmessage 
  

def main(): 
    
    
    p, d, e1, e2 = getpublickey()
    print("B Public Key  (p):",p)
    print("e1 is that:",e1)
    print("e2 is that:",e2)
    print("B Private Key (d):",d)
       
    message = input("Please enter the message to encrypt:")
    encryptedmessage, c1 = Encryption(message, p, e1, e2)
    decryptedmessage = Decryption(encryptedmessage, p, d, e1, c1)
     
    decmsg = ''.join(decryptedmessage) 
    print("\nDecrypted Message :", decmsg);
    
    
if __name__ == '__main__': 
    main() 

     


# In[ ]:




