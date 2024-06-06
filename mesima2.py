


def encrypt(encryNum,png, whichImage_to_get):
    with open(png, "rb") as image:
        read_image = image.read()
        bytes_arr = bytearray(read_image)

    encryptedResult = bytearray()
    for byte in bytes_arr:
        encryptedResult.append(byte ^ encryNum)

    backToImg = bytearray()
    for byte in encryptedResult:
        backToImg.append(byte ^ encryNum)
    if(whichImage_to_get == "backToImg"):
        return backToImg
    if(whichImage_to_get == "encryptedResult"):
        return encryptedResult
    
print(encrypt(5, "dog.png", "backToImg"))