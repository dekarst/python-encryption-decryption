import re

codes = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}

# Encrytion
def encryptor(message):
    if message == '':
        return 'Empty message'
    if bool(re.search(r'\d', message)):
        return 'Invalid message'

    passout = []
    for character in message:
        code = codes.get(character.lower(), False)
        if not code:
            passout.append(character)
        else:
            passout.append(str(code))

    return ''.join(passout)


# Decrytion
def getCodeKey(char, dic):
        for k, v in dic.items():
            if str(v) == char:
                return k
        return False

def decryptor(message):
    if message == '':
        return 'Empty message'

    passout = []
    for character in message:
        key = getCodeKey(character, codes)
        if not key:
            passout.append(character)
        else:
            passout.append(key)

    return ''.join(passout)


# Unit Test
def test_encryptor():
    assert encryptor('') == 'Empty message', 'Should be "Empty message"'
    assert encryptor('a1b') == 'Invalid message', 'Should be "Invalid message"'
    assert encryptor('This is test') == 'Th3s 3s t2st', 'Should be "Th3s 3s t2st"'

def test_decryptor():
    assert decryptor('') == 'Empty message', 'Should be "Empty message"'
    assert decryptor('1n4th2r m2ss1g2 h2r2!') == 'another message here!', 'Should be "another message here!"'

if __name__ == '__main__':
    test_encryptor()
    test_decryptor()
    print('Everything passed')
