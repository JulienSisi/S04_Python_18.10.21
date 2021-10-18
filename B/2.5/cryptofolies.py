# Cryptofolies

def caesar_cipher(text, shift):
    input=raw_input('Input text here: ')
    a = ord('a')
    return ''.join(
        chr((ord(char) - a + shift) % 26 + a) if 'a' <= char <= 'z' else char
        for char in text.lower())

caesar_cipher(raw_input('Input text here: '), 3)
print (caesar_cipher)
