text = input("Introduce un texto: ")
cipher = ''

for char in text:
    if char == ' ':
        cipher += ' '
        continue
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cipher += chr(code)

print(cipher)