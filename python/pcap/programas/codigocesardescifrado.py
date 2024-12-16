cipher = input('Ingresa tu texto encriptado: ')
text = ''

for char in cipher:
    if char == ' ':
        text += ' '
        continue
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    text += chr(code)

print(text)