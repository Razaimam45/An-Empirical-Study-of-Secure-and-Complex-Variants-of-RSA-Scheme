# ************* HRSA Permormance Table Code ***************

# In[20]:
import time

#X RSA Latest code

#key gen start-----------------------------------------------
start_key_gen_time = time.time()
# print("Key Generation:\n");
a = generate_prime_number(10)
b = generate_prime_number(10)
c = generate_prime_number(10)
d = generate_prime_number(10)


# print("Is p1=",p1, "prime ? ", is_prime(p1));
# print("Is p2=",p2,"prime ?",is_prime(p2));
# print("Is p3=",p3, "prime ? ", is_prime(p3));
# print("Is p4=",p4,"prime ?",is_prime(p4)); #CORRECT


x = a*b;
y = c*d;
M = x*y; # evaluating N
# print("\nx=",x);
# print("y=",y);
# print("N=",N); #CORRECT


phi_x = (a-1)*(b-1); # evaluating Euler Totients: phi
phi_y = (c-1)*(d-1);
phi_M = phi_x*phi_y;
# print("phi(n)=", phi_n);
# print("phi(m)=", phi_m);
# print("phi(N)=", phi_N); #CORRECT


#E1, E2 calculation
p1 = ZZ.random_element(phi_x);
while (gcd(p1, phi_x) != 1):
    p1 = ZZ.random_element(phi_x) #choosing e1
print("\np1 =",p1);
print("*p1 < phi_x=",p1 < phi_x); #checking conditions for e1
print("*gcd(p1,phi_x)=",gcd(p1,phi_x)); #CORRECT

p2 = ZZ.random_element(phi_y)
while (gcd(p2, phi_y) != 1):
    p2 = ZZ.random_element(phi_y) #choosing e2
print("\np2 =",p2);
print("*p2 < phi_y=",p2 < phi_y); #checking conditions for e1
print("*gcd(p2,phi_y)=",gcd(p2,phi_y)); #CORRECT

P1 = power_mod(p1,p2,M)
# print("\nE1=",E1); #CORRECT

P = ZZ.random_element(phi_M*P1)
while (gcd(P, phi_M*P1) != 1):
    P = ZZ.random_element(phi_M*P1) #choosing e2
print("\nP=",P); #CORRECT
print("1<P<phi_M*P1",1<P<phi_M*P1)
print("*gcd(P,phi_M*P1)=",gcd(P,phi_M*P1)); #CORRECT

Q = inverse_mod(P,phi_M*P1)
print("\nQ=",Q); #CORRECT
# print("\nD bits",D.nbits())

w = ZZ.random_element(x)
if(a>b):
    while (gcd(w,x) != 1 or ((x-a) < w < x)==False):
        w = ZZ.random_element(x)
    print("\nw=",w)
    print("*gcd(w,x)=",gcd(w,x))
    print("*x-a < w < x",(x-a) < w < x)

elif(a<b):
    while (gcd(w,x) != 1 or ((x-b) < w < x)==False):
        w = ZZ.random_element(x)
    print("\nw=",w)
    print("*gcd(w,x)=",gcd(w,x))
    print("*x-b < w < x",(x-b) < w < x)

# small n is the component here
print("\npublic key = (",w, ",",P,")"); #Generated Key pairs
print("private key = (",w, ",",Q,")\n");

final_key_gen_time = time.time()
#key gen finish----------------------------------------------

total_key_gen_time = final_key_gen_time - start_key_gen_time
print("\nTotal Key generation time taken in seconds: ", total_key_gen_time )

#Encryption start--------------------------------------------
start_encrypt_time = time.time()
# print("Encryption & Decryption:\n"); 
M = 59; #print("original msg=",M) #original message m
C = power_mod(M,P,w); #print("encrypted msg=",C) #encrypted message c
finish_encrypt_time = time.time()
#Encryption finish---------------------------------------------

total_encrypt_time = finish_encrypt_time - start_encrypt_time
print("\nTotal encrypt taken in seconds: ", total_encrypt_time )

#Decryption start----------------------------------------------
start_decrypt_time = time.time() 
decrypt_msg = power_mod(C,Q,w) # decrypting 
print("decrypted msg=",decrypt_msg)# so m was correctly decrypted
finish_decrypt_time = time.time()
#Decryption finish----------------------------------------------

total_decrypt_time = finish_decrypt_time - start_decrypt_time
print("\nTotal decrypt time taken in seconds: ", total_decrypt_time )


total_time_taken = total_key_gen_time + total_encrypt_time + total_decrypt_time
print("\n\nTotal algorithm time taken in seconds: ", total_time_taken)
print("\nIs decrypted msg & original msg same?", (decrypt_msg==M))