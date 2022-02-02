from cryptography.fernet import Fernet


class Cryptography:
    """
    Class used in cryptography operations
    """
    def __init__(self, filename='crypto.key'):
        """
        Initialize object with default or given crypto key.

        :param filename: string leading to file with crypto key
        """
        with open(filename, 'rb') as filekey:
            self.key = filekey.read()
        self.fernet = Fernet(self.key)

    def decrypt(self, filename):
        """
        Decrypt any given file with default key

        :param filename: string - name of file to decrypt
        :return: decrypted file
        """
        with open(filename, 'rb') as encrypted_file:
            data = encrypted_file.read()
            data = self.fernet.decrypt(data)
        with open(filename, 'wb') as file:
            file.write(data)

    def encrypt(self, filename):
        """
        Encrypt any given file with default key

        :param filename: string - name of file to encrypt
        :return: encrypted file
        """
        with open(filename, 'rb') as file:
            original = file.read()
        encrypted = self.fernet.encrypt(original)
        with open(filename, 'wb') as encrypted_file:
            encrypted_file.write(encrypted)

    def replace_key(self, filename='crypto.key'):
        """
        Generate and replace default key

        :param filename: string - name of file to save the key
        :return: File with new crypto key
        """
        self.key = Fernet.generate_key()
        with open(filename, 'wb') as filekey:
            filekey.write(self.key)
