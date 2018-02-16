
def public_Key(Alpha, element, q):
    Y_key = (Alpha ** element) % q
    return Y_key

def key_generation(Alpha, element, q):
    K = (Alpha ** element) % q
    return K

def check_success(element, elements):
    if element == elements:
        decision = print("Public KEYS are same, The Exchange is SUCCESSFUL")
    else:
        decision = print("Public KEYS are different")
    return decision

def encrypt_another(plaintext, key):
    ciphertext = ""
    for c in plaintext.upper():
        ciphertext += I2L[(L2I[c] + key) % 36]
    return ciphertext

def decrypt_another(ciphertext, key):
    plaintext = ""
    for c in ciphertext.upper():
        plaintext += I2L[(L2I[c] - key) % 36]
    return plaintext


if __name__ == '__main__':
    try:
        input = raw_input
    except NameError:
        pass
    try:
        chr = unichr
    except NameError:
        pass

    q = int(input("\nPlease Enter Common Prime value of q: "))
    a = int(input("Please Enter Primitive root Alpha value : "))
    # q = 23
    # a = 5

    A = int(input("\nPlease Enter Private Key of Party A : "))
    B = int(input("Please Enter Private Key of Party B : "))
    # A = 6
    # B = 15

    L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", range(1, 37)))
    I2L = dict(zip(range(1, 37), "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"))
    print(L2I)
    print(I2L)

    print ("The Entered Common Prime value: \n q = " + str(q) + " , \n and Primitive root of \n Alpha value = " + str(a) + "\n")
    print ("The Entered Private Key of Party: \n A = " + str(A) + ", \n and Private Key of Party: \n B = " + str(B) + "\n")

    Y_A = public_Key(a, A, q)
    Y_B = public_Key(a, B, q)
    print("The Calculation Key of User: \n A = " + str(Y_A) + "\n")
    print("The Calculation Key of User: \n B = " + str(Y_B) + "\n")

    K_A = key_generation(Y_B, A, q)
    K_B = key_generation(Y_A, B, q)
    print("The Generated Public Key of User: \n A = " + str(K_A) + "\n")
    print("The Generated Public Key of User: \n B = " + str(K_B) + "\n")

    check_success(K_A, K_B)

    plaintext = "helloIamcommingon23offebruary"
    print("\nT23he PlainText is: \n " + plaintext + "\n" + "\n The PlainText in UPPERCASE is: \n " + plaintext.upper() + "\n")

    ciphertext = encrypt_another(plaintext, K_A)
    print("\nThe Generated CipherText is: \n ", ciphertext)
    plain = decrypt_another(ciphertext, K_A)
    print("\nThe Decrypted CipherText is: \n ", plain)
