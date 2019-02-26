from Crypto.Cipher import XOR
import base64

class Credentials:

  def encrypt(self, key, plaintext):
    cipher = XOR.new(key)
    return base64.b64encode(cipher.encrypt(plaintext))

  def decrypt(self, key, ciphertext):
    cipher = XOR.new(key)
    return cipher.decrypt(base64.b64decode(ciphertext))