# ************* Parallel RSA Code ***************

# In[20]:
import time
from multiprocessing import Pool
import random

#PRIME GENERATION FUNCTION START*****
from random import randrange, getrandbits
def is_prime(n, k=128):
    """ Test if a number is prime
        Args:
            n -- int -- the number to test
            k -- int -- the number of tests to do
        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    flag=1
    p=Pool()
    results = [p.apply_async(primetest, args=(s,r,n,)) for x in range(k)]
    
    for k in results:
        output = [k.get()]
        #print("VALUE OF OUTPUT",k.get())
        if k.get()==False:
            flag=0
            break
        
    
    if flag==0:
        p.close()
        p.join()
        return False

    else:
        p.close()
        p.join()
        return True

            
    #u=primetest(s,r,n,k)
def primetest(s,r,n):
    #for _ in range(k):
    #print("Test.value in primetest", test.value)
    a = randrange(2, n - 1)
    x = pow(a, r, n)
    if x != 1 and x != n - 1:
        j = 1
        while j < s and x != n - 1:
            x = pow(x, 2, n)
            if x == 1:
                return False
            j += 1
        if x != n - 1:
            return False
    return True
def generate_prime_candidate(length):
    """ Generate an odd integer randomly
        Args:
            length -- int -- the length of the number to generate, in bits
        return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1
    return p
def generate_prime_number(length=1024):
    """ Generate a prime
        Args:
            length -- int -- length of the prime to generate, in          bits
        return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
        #print("value of p is",p)
    return p
#print(generate_prime_number())
#PRIME GENERATION FUNCTION END*****

#GCD FUNCTION START*****
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
#GCD FUNCTION END*****

#MOD INVERSE FUNCTION START*****
def modInverse(a, m):
    m0 = m
    y = 0
    x = 1
 
    if (m == 1):
        return 0
 
    while (a > 1):
 
        # q is quotient
        q = a // m
 
        t = m
 
        # m is remainder now, process
        # same as Euclid's algo
        m = a % m
        a = t
        t = y
 
        # Update x and y
        y = x - q * y
        x = t
 
    # Make x positive
    if (x < 0):
        x = x + m0
 
    return x
#MOD INVERSE FUNCTION END*****


# Algorithm START >>>>>>>>>>>>>>>>
for i in range(1):
    #key gen start-----------------------------------------------
    start_key_gen_time = time.time()
    # print("Key Generation:\n");
    p = generate_prime_number(50)
    q = generate_prime_number(50)
    r = generate_prime_number(50)
    s = generate_prime_number(50)

    print("Is p=",p, "prime ? ", is_prime(p));
    print("Is q=",q,"prime ?",is_prime(q));
    print("Is r=",r, "prime ? ", is_prime(r));
    print("Is s=",s,"prime ?",is_prime(s)); #CORRECT
    print(p.bit_length(),q.bit_length(),r.bit_length(),s.bit_length())

    x = p*q;
    y = r*s;
    N = x*y; # evaluating N

    phi_x = (p-1)*(q-1); # evaluating Euler Totients: phi
    phi_y = (r-1)*(s-1);
    phi_N = phi_x*phi_y;

    E1 = random.randrange(1, phi_x)
    g1 = gcd(E1, phi_x)
    while g1 != 1:
        E1 = random.randrange(1, phi_x)
        g1 = gcd(E1, phi_x)

    E2 = random.randrange(1, phi_y)
    g2 = gcd(E2, phi_y)
    while g2 != 1:
        E2 = random.randrange(1, phi_y)
        g2 = gcd(E2, phi_y)

    E = (E1 * E2)%N
    D = modInverse(E, phi_N)

    # #print((E*D)%phi_N)

    # print("\npublic key = (",N, ",",E,")"); #Generated Key pairs
    # print("private key = (",N, ",",D,")\n");

    final_key_gen_time = time.time()
    # #key gen finish----------------------------------------------

    total_key_gen_time = final_key_gen_time - start_key_gen_time
    print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )

#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
M = 59; #print("original msg=",M) #original message m
C = pow(M,E,N); #print("encrypted msg=",C) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = pow(C,D,N) # decrypting 
# print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seco256nds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))