from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

class RSACipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None

    def generate_keys(self):
        """Генерація пари ключів RSA."""
        self.private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048
        )
        self.public_key = self.private_key.public_key()
        print("Ключі згенеровано успішно!")

    def save_keys(self):
        """Збереження ключів у файли."""
        private_key_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_key_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open("private_key.pem", "wb") as private_file:
            private_file.write(private_key_pem)
        with open("public_key.pem", "wb") as public_file:
            public_file.write(public_key_pem)
        print("Ключі збережено у файли private_key.pem та public_key.pem.")

    def load_keys(self):
        """Завантаження ключів з файлів."""
        with open("private_key.pem", "rb") as private_file:
            self.private_key = serialization.load_pem_private_key(
                private_file.read(),
                password=None
            )
        with open("public_key.pem", "rb") as public_file:
            self.public_key = serialization.load_pem_public_key(public_file.read())
        print("Ключі завантажено успішно!")

    def encrypt(self, message):
        """Шифрування повідомлення."""
        encrypted = self.public_key.encrypt(
            message.encode('utf-8'),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Повідомлення зашифровано!")
        return encrypted

    def decrypt(self, encrypted_message):
        """Розшифрування повідомлення."""
        decrypted = self.private_key.decrypt(
            encrypted_message,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        print("Повідомлення розшифровано!")
        return decrypted.decode('utf-8')

def main():
    rsa_cipher = RSACipher()

    while True:
        print("\nМеню:")
        print("1. Генерація ключів")
        print("2. Зберегти ключі у файли")
        print("3. Завантажити ключі з файлів")
        print("4. Шифрувати повідомлення")
        print("5. Розшифрувати повідомлення")
        print("6. Вихід")

        choice = input("Оберіть опцію: ")
        if choice == "1":
            rsa_cipher.generate_keys()
        elif choice == "2":
            rsa_cipher.save_keys()
        elif choice == "3":
            rsa_cipher.load_keys()
        elif choice == "4":
            message = input("Введіть повідомлення для шифрування: ")
            encrypted_message = rsa_cipher.encrypt(message)
            print("Зашифроване повідомлення:", encrypted_message)
        elif choice == "5":
            encrypted_message = input("Введіть зашифроване повідомлення (у байтах): ")
            try:
                encrypted_message = eval(encrypted_message)  # Перетворення рядка на байти
                decrypted_message = rsa_cipher.decrypt(encrypted_message)
                print("Розшифроване повідомлення:", decrypted_message)
            except Exception as e:
                print("Помилка при розшифруванні:", str(e))
        elif choice == "6":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
