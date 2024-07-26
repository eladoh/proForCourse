import hashlib

hash_value = "3cc6520a6890b92fb55a6b3d657fd1f6"

for num in range(100000, 10000000):
    number_str = str(num).encode()
        
    md5 = hashlib.md5()
    md5.update(number_str)
    hash_hex = md5.hexdigest()
    
    if hash_hex == hash_value:
        print(num)