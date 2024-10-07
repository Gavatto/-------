def linear_shift_key(p, A, B):
    return A * p + B

def nonlinear_shift_key(p, A, B, C):
    return A * (p ** 2) + B * p + C

def keyword_shift_key(text, keyword):
    repeated_key = (keyword * (len(text) // len(keyword) + 1))[:len(text)]
    return [ord(char) - ord('A') for char in repeated_key]

def trithemius_cipher(text, key_type, A=0, B=0, C=0, keyword=""):
    encrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            if key_type == "linear":
                k = linear_shift_key(i, A, B)
            elif key_type == "nonlinear":
                k = nonlinear_shift_key(i, A, B, C)
            elif key_type == "keyword":
                k = keyword_shift_key(text, keyword)[i]
            encrypted_text += chr((ord(char) - offset + k) % 26 + offset)
        else:
            encrypted_text += char
    return encrypted_text

def trithemius_decipher(text, key_type, A=0, B=0, C=0, keyword=""):
    decrypted_text = ""
    for i, char in enumerate(text):
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            if key_type == "linear":
                k = linear_shift_key(i, A, B)
            elif key_type == "nonlinear":
                k = nonlinear_shift_key(i, A, B, C)
            elif key_type == "keyword":
                k = keyword_shift_key(text, keyword)[i]
            decrypted_text += chr((ord(char) - offset - k) % 26 + offset)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Шифр Тритеміуса")
    choice = input("Оберіть дію (1 - шифрування, 2 - розшифрування): ")
    text = input("Введіть текст: ")
    key_type = input("Виберіть тип ключа (linear, nonlinear, keyword): ")

    if key_type == "linear":
        A = int(input("Введіть A: "))
        B = int(input("Введіть B: "))
        if choice == "1":
            print("Зашифрований текст:", trithemius_cipher(text, key_type, A=A, B=B))
        else:
            print("Розшифрований текст:", trithemius_decipher(text, key_type, A=A, B=B))

    elif key_type == "nonlinear":
        A = int(input("Введіть A: "))
        B = int(input("Введіть B: "))
        C = int(input("Введіть C: "))
        if choice == "1":
            print("Зашифрований текст:", trithemius_cipher(text, key_type, A=A, B=B, C=C))
        else:
            print("Розшифрований текст:", trithemius_decipher(text, key_type, A=A, B=B, C=C))

    elif key_type == "keyword":
        keyword = input("Введіть гасло: ").upper()
        if choice == "1":
            print("Зашифрований текст:", trithemius_cipher(text, key_type, keyword=keyword))
        else:
            print("Розшифрований текст:", trithemius_decipher(text, key_type, keyword=keyword))
    else:
        print("Невірний тип ключа.")

if __name__ == "__main__":
    main()
