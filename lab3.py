class BookCipher:
    def __init__(self, poem, size=10):
        self.size = size
        self.grid = self._create_grid(poem)

    def _create_grid(self, text):
        text = text.replace(" ", "").upper()
        text = text.replace("Щ", "Ш")  # Замінюємо "Щ" на "Ш" як вказано в завданні
        grid = []
        row = []
        for char in text:
            if len(row) < self.size:
                row.append(char)
            if len(row) == self.size:
                grid.append(row)
                row = []
        if row:  # Додаємо останній неповний рядок, якщо він є
            grid.append(row)
        return grid

    def _find_position(self, char):
        for r, row in enumerate(self.grid):
            for c, grid_char in enumerate(row):
                if grid_char == char:
                    return r + 1, c + 1  # Повертаємо координати, починаючи з 1
        return None, None

    def encrypt(self, message):
        message = message.upper().replace("Щ", "Ш")
        encrypted_message = []
        for char in message:
            row, col = self._find_position(char)
            if row is not None and col is not None:
                encrypted_message.append(f"{row}/{col}")
        return ", ".join(encrypted_message)

    def decrypt(self, encrypted_message):
        decrypted_message = ""
        pairs = encrypted_message.split(", ")
        for pair in pairs:
            row, col = map(int, pair.split("/"))
            try:
                decrypted_message += self.grid[row - 1][col - 1]
            except IndexError:
                decrypted_message += "?"
        return decrypted_message

def main():
    poem = input("Введіть вірш для ключа: ")
    cipher = BookCipher(poem)
    
    choice = input("Оберіть дію (1 - шифрування, 2 - розшифрування): ")
    if choice == "1":
        message = input("Введіть повідомлення для шифрування: ")
        encrypted = cipher.encrypt(message)
        print("Зашифроване повідомлення:", encrypted)
    elif choice == "2":
        encrypted_message = input("Введіть зашифроване повідомлення (формат: CC/SS): ")
        decrypted = cipher.decrypt(encrypted_message)
        print("Розшифроване повідомлення:", decrypted)
    else:
        print("Невірний вибір.")

if __name__ == "__main__":
    main()
