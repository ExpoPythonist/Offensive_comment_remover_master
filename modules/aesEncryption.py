from Crypto.Cipher import AES
import base64
import os


class aesEncryption:
    def __init__(self):
        # the block size for the cipher object; must be 16, 24, or 32 for AES
        self.BLOCK_SIZE = 32
        # the character used for padding--with a block cipher such as AES, the value
        # you encrypt must be a multiple of BLOCK_SIZE in length.  This character is
        # used to ensure that your value is always a multiple of BLOCK_SIZE
        self.PADDING = '{'

        # generate a random secret key
        # self.secret = os.urandom(self.BLOCK_SIZE)
        self.secret = b'\x92\x19\x1e\xd2\xc7\xfa\x13\x1fg\x9e\x9fBc\xd0V<\xc10\xbdY+\x04n\xaa&[G\xdf<{\xdc\x80'

        # create a cipher object using th random secret
        self.cipher = AES.new(self.secret, AES.MODE_EAX)

    # one-liner to sufficiently pad the text to be encrypted
    def pad(self, s):
        return s + (self.BLOCK_SIZE - len(s) % self.BLOCK_SIZE) * self.PADDING

    # one-liners to encrypt/encode and decrypt/decode a string
    # encrypt with AES, encode with base64
    def EncodeAES(self, s):
        print('see===> ', s)
        return base64.b64encode(self.cipher.encrypt(self.pad(s)))

    def DecodeAES(self, e):
        return str(self.cipher.decrypt(base64.b64decode(e)), 'utf-8').rstrip(self.PADDING)


if __name__ == "__main__":

    # obj = aesEncryption()

    # encoded = obj.EncodeAES('password')
    # print('Encrypted string:', encoded)

    # decoded = obj.DecodeAES(encoded)
    # print('Decrypted string:', decoded)
    pass
