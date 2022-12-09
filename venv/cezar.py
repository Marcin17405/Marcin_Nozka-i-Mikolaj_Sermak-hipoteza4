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
    for i in range(len(encrypted)):
        key =i+1
        if (ord(encrypted[i]) - key < 97):
            decrypted += chr(ord(encrypted[i]) - key + 26)
        else:
            decrypted += chr(ord(encrypted[i]) - key)
    return decrypted


print("Zakodowane",encrypt("abc"))
print("Odkodowane",decrypt("bdf"))