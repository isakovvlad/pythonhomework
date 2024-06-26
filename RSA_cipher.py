import random, math

class RSA_cipher:

    #Проверка на простоту числа
    @staticmethod
    def number_is_prime(number):
        if number == 1:
            return False
        if number % 2 == 0:
            return number == 2
        for i in range(3, int(math.sqrt(number)) + 1, 2):
            if number % i == 0:
                return False
        return True

    #НОД
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    #Генерация простого числа
    def generate_prime_number(self, lower_limit = 0, upper_limit = 1000, prime_number = 0):
        while not self.number_is_prime(prime_number):
            prime_number = random.randint(lower_limit, upper_limit)
        return prime_number

    #Генерация приватного и публичного ключа
    def generate_key_pair(self):
        p, q = self.generate_prime_number(), self.generate_prime_number()
        f_n = (p - 1) * (q - 1)
        e = 2
        tmp = self.gcd(e, f_n)
        while tmp != 1:
            e += 1
            tmp = self.gcd(e, f_n)
        d = pow(e, -1, f_n)
        pblc_key, prvt_key = (e, p * q), (d, p * q)
        return pblc_key, prvt_key

    #Шифрование
    @staticmethod
    def encrypt_message(message, public_key):
        e, n = public_key
        ls = []
        for x in message:
            ls.append(str(pow(ord(x), e, n)))
        return ls
    
    #Дешифрование
    @staticmethod
    def decrypt_message(cipher_text, private_key):
        d, n = private_key
        ls = []
        for x in cipher_text:
            ls.append(chr(pow(int(x), d, n)))
        return "".join(ls)
    
public_key, private_key = RSA_cipher().generate_key_pair()
user_message = input("enter a message: ")
encrypted_message = RSA_cipher().encrypt_message(user_message, public_key)
decrypted_message = RSA_cipher().decrypt_message(encrypted_message, private_key)
print("public and private keys:", public_key, private_key)
print("encrypted message: ", "".join(encrypted_message))
print("decrypted message: ", decrypted_message)
