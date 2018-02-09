
# Function for finding the gcd of e and phi
def gcd(e, phi):
    while phi != 0:
        for e in phi:
            e, phi = phi, e % phi
            print(e)
    return e


# Function for cheching e prime numbers
def is_prime(phi):
    x = []
    # prime numbers are greater than 1
    if phi > 1:
        for i in range(2, phi):
            if(phi < 5):
                x = (1, 2, 3, 4)
                return x
            else:
                if (phi % i) != 0 :
                    if ((i % 2) == 0):
                        pass
                    else:
                        x.append(i)
    return x

# Function for Ecrypting the Document
def encrypt(M, e, n):
    try:
        if M < n:
            C = (M ** e) % n
            return C
    except:
        return (" Plain Text should be less than n = ", n)

# Function for Decrypting the Document
def decrypt(C, d, n):
    try:
        while C:
            M = (C ** d) % n
            return M
    except:
        return (" Plain Text should be less than n = ", n)


if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    try:
        chr = unichr
    except NameError:
        pass

    p = int(input("Please Enter Prime value of p: "))
    q = int(input("Please Enter Prime value of q: "))

    print ("The Entered Prime Values: \n p = " + str(p) + ", q = " + str(q) + "\n")

    n = p * q
    print ("n is equal to : " + str(n) + "\n")

    phi = (p - 1) * (q - 1)
    print ("The Euler's totient function [phi(n)] = " + str(phi) + "\n")

    print ("The Generated e array list is : \n" + str(is_prime(phi)) + "\n")

    e = int(input("Please Choose an e from the array list above : "))
    d = e

    print ("\nThe Generated public Key is {e = " + str(e) + ", n = " + str(n) + ").\n")
    print ("\nThe Generated private Key is {d = " + str(e) + ", n = " + str(n) + ").\n")


    M = int(input("Please Enter Plain Text to Encrypt: "))
    N = int(input("Please Enter Plain Text to Encrypt: "))


    E = encrypt(M, e, n)
    print ("\nThe Generated Cipher Text is = " + str(E) + "\n")
    D = encrypt(N, e, n)
    print ("\nThe Generated Cipher Text is = " + str(D) + "\n")
    print ("\nThe Whole Generated Cipher Text is = " + str(E) + ", and " + str(D) + "\n")


    F = decrypt(E, e, n)
    print ("\nThe Decrypted Cipher Text is = " + str(F) + "\n")
    G = decrypt(D, e, n)
    print ("\nThe Decrypted Cipher Text is = " + str(G) + "\n")
    print ("\nThe Whole Decrypted Cipher Text is = " + str(F) + ", and " + str(G) + "\n")