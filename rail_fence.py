def printFence(fence):
    for rail in range(len(fence)):
        print ''.join(fence[rail])
    
def encryptFence(plain, rails, offset=0, debug=False):
    cipher = ''

    # offset
    plain = '#'*offset + plain

    length = len(plain)
    fence = [['#']*length for _ in range(rails)]

    # build fence
    rail = 0
    for x in range(length):
        fence[rail][x] = plain[x]
        if rail >= rails-1:
            dr = -1
        elif rail <= 0:
            dr = 1
        rail += dr

    # print pretty fence
    if debug:
        printFence(fence)

    # read fence
    for rail in range(rails):
        for x in range(length):
            if fence[rail][x] != '#':
                cipher += fence[rail][x]
    return cipher

    # print pretty fence
    if debug:
        printFence(fence)

    # read fence
    for i in range(length):
        for rail in range(rails):
            if fence[rail][i] != '#':
                plain += fence[rail][i]
    return plain


if __name__ == "__main__":
    plain = "defendhim"
    print plain
    cipher = encryptFence(plain, 3, offset=4, debug=True)
    print cipher
    