niezaszyfrowany = "cezar"
zaszyfrowany = ""

for i in range(len(niezaszyfrowany)):
    klucz = i+1
    if ord(niezaszyfrowany[i]) > 122 - klucz:
        zaszyfrowany += chr(ord(niezaszyfrowany[i]) + klucz - 26)
    else:
        zaszyfrowany += chr(ord(niezaszyfrowany[i]) + klucz)

print("Zaszyfrowany tekst:", zaszyfrowany)