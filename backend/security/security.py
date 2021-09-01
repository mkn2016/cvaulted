from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes


class Security(object):
    key:bytes = get_random_bytes(16)
    iv:bytes = get_random_bytes(16)

    @staticmethod
    def encrypt(data):
        cipher = AES.new(Security.key, AES.MODE_CBC, Security.iv)
        if isinstance(data, int):
            data = str(data)
            cipher_text = cipher.encrypt(pad(data.encode(), AES.block_size))

        else:
            cipher_text = cipher.encrypt(pad(data.encode(), AES.block_size))
        
        return str(cipher_text)

    @staticmethod
    def decrypt(data):
        print(type(data))
        cipher = AES.new(Security.key, AES.MODE_CBC, iv=Security.iv)
        plain_text = unpad(cipher.decrypt(data), AES.block_size)
        return plain_text.decode()

