def hill(code): 
    Key = [[3,24],
                     [25,17]]
    
    code = code.lower()
    output = [[0],[0]]
    counter = 0
    for character in code:
        number = ord(character) - 97
        output[counter][0] = number
        counter += 1

    result = [[0],[0]]

    for i in range(len(Key)):
       for j in range(len(output[0])):
           for k in range(len(output)):
               result[i][0] += Key[i][k] * output[k][j]

    unCiphered = ""
    for r in result:
       numeric_letter = r[0] % 26
       val = chr(numeric_letter + 97)
       unCiphered = unCiphered + val

    return unCiphered

def main():
    code = 'Mississippi';
    print code;
    plaintext = plaintext + hill(ciphertext);
    print plaintext;
                    
main()