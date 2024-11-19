from sympy import mod_inverse

class KnapsackCipher:
    def __init__(self):
        self.private_key = None
        self.public_key = None
        self.m = None
        self.t = None

    def generate_keys(self, superincreasing_sequence, m, t):
        """
        Генерація відкритого та закритого ключів
        """
        if m <= sum(superincreasing_sequence) or gcd(t, m) != 1:
            raise ValueError("Неправильні параметри m або t.")
        
        self.private_key = superincreasing_sequence
        self.m = m
        self.t = t
        self.public_key = [(t * b) % m for b in superincreasing_sequence]

    def encrypt(self, message):
        """
        Шифрування повідомлення.
        """
        binary_message = ''.join(format(ord(char), '08b') for char in message)
        blocks = [binary_message[i:i + len(self.public_key)] for i in range(0, len(binary_message), len(self.public_key))]

        encrypted_blocks = []
        for block in blocks:
            block = [int(bit) for bit in block]
            while len(block) < len(self.public_key):
                block.append(0)  # Додати 0 для заповнення блоку
            encrypted_blocks.append(sum(block[i] * self.public_key[i] for i in range(len(block))))

        return encrypted_blocks

    def decrypt(self, encrypted_blocks):
        """
        Розшифрування повідомлення.
        """
        t_inverse = mod_inverse(self.t, self.m)
        binary_message = ''

        for c in encrypted_blocks:
            c_prime = (c * t_inverse) % self.m
            block = []
            for b in reversed(self.private_key):
                if c_prime >= b:
                    block.append(1)
                    c_prime -= b
                else:
                    block.append(0)
            binary_message += ''.join(map(str, reversed(block)))

        message = ''.join(chr(int(binary_message[i:i + 8], 2)) for i in range(0, len(binary_message), 8))
        return message

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    knapsack_cipher = KnapsackCipher()

    # Ключі
    superincreasing_sequence = [2, 3, 7, 14, 30, 57, 120]
    m = 255
    t = 41

    print("Генерація ключів...")
    knapsack_cipher.generate_keys(superincreasing_sequence, m, t)
    print("Закритий ключ (суперзростаюча послідовність):", knapsack_cipher.private_key)
    print("Відкритий ключ:", knapsack_cipher.public_key)

    # Повідомлення
    message = "HELLO"
    print("\nОригінальне повідомлення:", message)

    # Шифрування
    encrypted = knapsack_cipher.encrypt(message)
    print("Зашифроване повідомлення:", encrypted)

    # Розшифрування
    decrypted = knapsack_cipher.decrypt(encrypted)
    print("Розшифроване повідомлення:", decrypted)

if __name__ == "__main__":
    main()
