from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
import os

class DESCipher:
    def __init__(self, key):
        self.key = key.ljust(8)[:8].encode('utf-8')  # Довжина ключа DES - 8 байт

    def encrypt(self, plaintext):
        cipher = DES.new(self.key, DES.MODE_CBC)  # Використовуємо режим CBC
        iv = cipher.iv
        padding_length = 8 - len(plaintext) % 8
        padded_plaintext = plaintext + chr(padding_length) * padding_length  # Додаємо паддінг

        encrypted_data = cipher.encrypt(padded_plaintext.encode('utf-8'))
        return iv + encrypted_data  # Повертаємо IV разом із зашифрованими даними

    def decrypt(self, encrypted_data):
        iv = encrypted_data[:8]  # Перші 8 байтів - це IV
        encrypted_data = encrypted_data[8:]

        cipher = DES.new(self.key, DES.MODE_CBC, iv)
        decrypted_data = cipher.decrypt(encrypted_data).decode('utf-8')
        padding_length = ord(decrypted_data[-1])  # Видаляємо паддінг
        return decrypted_data[:-padding_length]

def save_to_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

def read_from_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

def main():
    key = "ABCDEFGH"  # Приклад ключа
    des_cipher = DESCipher(key)
    
    choice = input("Оберіть дію (1 - шифрування, 2 - розшифрування): ")
    
    if choice == "1":
        plaintext = input("Введіть текст для шифрування: ")
        encrypted_data = des_cipher.encrypt(plaintext)
        save_to_file("encrypted_des.bin", encrypted_data)
        print("Дані зашифровані та збережені у файл 'encrypted_des.bin'")
        
    elif choice == "2":
        encrypted_data = read_from_file("encrypted_des.bin")
        decrypted_text = des_cipher.decrypt(encrypted_data)
        print("Розшифрований текст:", decrypted_text)
        
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()
