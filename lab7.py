from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization

class DigitalSignature:
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
        print("Ключі успішно згенеровані!")

    def save_keys(self):
        """Збереження ключів у файли."""
        private_pem = self.private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        public_pem = self.public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open("private_key.pem", "wb") as private_file:
            private_file.write(private_pem)
        with open("public_key.pem", "wb") as public_file:
            public_file.write(public_pem)
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
        print("Ключі успішно завантажено!")

    def sign_message(self, message):
        """Підписування повідомлення."""
        signature = self.private_key.sign(
            message.encode('utf-8'),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        print("Повідомлення підписано!")
        return signature

    def verify_signature(self, message, signature):
        """Перевірка цифрового підпису."""
        try:
            self.public_key.verify(
                signature,
                message.encode('utf-8'),
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            print("Підпис успішно перевірено!")
            return True
        except Exception as e:
            print("Перевірка підпису не вдалася:", e)
            return False

def main():
    ds = DigitalSignature()

    while True:
        print("\nМеню:")
        print("1. Генерація ключів")
        print("2. Зберегти ключі у файли")
        print("3. Завантажити ключі з файлів")
        print("4. Підписати повідомлення")
        print("5. Перевірити підпис")
        print("6. Вихід")

        choice = input("Оберіть опцію: ")
        if choice == "1":
            ds.generate_keys()
        elif choice == "2":
            ds.save_keys()
        elif choice == "3":
            ds.load_keys()
        elif choice == "4":
            message = input("Введіть повідомлення для підписання: ")
            signature = ds.sign_message(message)
            print("Підпис:", signature.hex())
        elif choice == "5":
            message = input("Введіть повідомлення для перевірки: ")
            signature_hex = input("Введіть підпис (у hex-форматі): ")
            signature = bytes.fromhex(signature_hex)
            result = ds.verify_signature(message, signature)
            print("Результат перевірки:", "Підпис дійсний" if result else "Підпис недійсний")
        elif choice == "6":
            print("Вихід із програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
