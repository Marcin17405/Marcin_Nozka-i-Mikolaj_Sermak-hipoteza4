def encrypt(decrypted):
    encrypted = ""
    for i in range(len(decrypted)):
        key = i + 1
        if ord(decrypted[i]) > 122 - key:
            encrypted += chr(ord(decrypted[i]) + key - 26)
        else:
            encrypted += chr(ord(decrypted[i]) + key)
    return encrypted

def decrypt(encrypted):
    decrypted = ""
    for i in encrypted:
        key = i + 1
        if (ord(encryped) - key < 97):
            decrypted += chr(ord(encrypted) - key + 26)
        else:
            decrypted += chr(ord(encrypted) - key)
    return decrypted


# print(encrypt("abc"))
print(decrypt("bdf"))