# Daniela Romaguera

def encode(password):
# this splits every character in string
    arr = [item for item in password]
# this turns every character into int
    arr = [eval(i) for i in arr]
    new = []
# adds 3 to every int
    for x in arr:
        x += 3
        new.append(x)
    new = ''.join(map(str, new))
    return new


def decode(password):
# splits every character in string
    dec = [item for item in password]
# turns every character into int
    dec = [eval(i) for i in dec]
    new = []
# subtracts 3 to every int
    for x in dec:
        x -= 3
        new.append(x)
    new = ''.join(map(str, new))
    return new


def main():
    quit = False
    while quit == False:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print('\nPlease enter an option: ', end='')
        opt = input()
        if opt == '1':
            print('Please enter your password to encode: ', end='')
            enc = input()
            new = encode(enc)
            print('Your password has been encoded and stored!\n')
        elif opt == '2':
            print(f'The encoded password is {new}, and the original password is {decode(new)}.\n')
        elif opt == '3':
            quit = True


if __name__ == '__main__':
    main()
