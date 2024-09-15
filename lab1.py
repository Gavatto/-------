def create_file():
    filename = input("Введіть назву файлу для створення: ")
    content = input("Введіть текст для збереження: ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Файл {filename} створено.")

def open_file():
    filename = input("Введіть назву файлу для відкриття: ")
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"Зміст файлу {filename}:")
            print(content)
            return content
    except FileNotFoundError:
        print(f"Файл {filename} не знайдено.")
        return None

def save_file(content):
    filename = input("Введіть назву файлу для збереження: ")
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)
    print(f"Файл {filename} збережено.")

def caesar_cipher(text, key, encrypt=True):
    result = ""
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            if encrypt:
                result += chr((ord(char) + key - offset) % 26 + offset)
            else:
                result += chr((ord(char) - key - offset) % 26 + offset)
        else:
            result += char
    return result

def encrypt_file():
    content = open_file()
    if content:
        key = int(input("Введіть ключ шифрування: "))
        encrypted_content = caesar_cipher(content, key, encrypt=True)
        print("Зашифрований текст:")
        print(encrypted_content)
        save_file(encrypted_content)

def decrypt_file():
    content = open_file()
    if content:
        key = int(input("Введіть ключ для розшифрування: "))
        decrypted_content = caesar_cipher(content, key, encrypt=False)
        print("Розшифрований текст:")
        print(decrypted_content)
        save_file(decrypted_content)

def show_info():
    print("Розробник: Ваше ім'я")

def main():
    while True:
        print("\nМеню:")
        print("1. Створити файл")
        print("2. Відкрити файл")
        print("3. Зберегти файл")
        print("4. Зашифрувати файл")
        print("5. Розшифрувати файл")
        print("6. Вивести інформацію про розробника")
        print("7. Вихід")
        
        choice = input("Оберіть опцію: ")
        
        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            content = input("Введіть текст для збереження: ")
            save_file(content)
        elif choice == "4":
            encrypt_file()
        elif choice == "5":
            decrypt_file()
        elif choice == "6":
            show_info()
        elif choice == "7":
            print("Вихід з програми...")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
