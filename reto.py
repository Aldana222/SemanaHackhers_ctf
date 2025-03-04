from Crypto.Cipher import AES
import base64

# Clave EXACTAMENTE la misma que se usó para cifrar
clave = b"clave_secreta_16"

# Flag cifrada en Base64 (salida de `cifrar_flag.py`)
flag_cifrada_b64 = "9xVWXEWN4EsZ9ss/87d5DuHA6K/E8YxlYIss7bu3PVA="

# Desencriptar y remover padding PKCS7
def unpad(s):
    return s[:-s[-1]]

def descifrar_flag():
    cipher = AES.new(clave, AES.MODE_ECB)
    flag_descifrada = cipher.decrypt(base64.b64decode(flag_cifrada_b64))
    return unpad(flag_descifrada).decode()

def verificar_flag():
    entrada = input("Introduce la flag: ").strip()
    
    if entrada == descifrar_flag():
        print("¡Correcto! Flag desbloqueada 🎉")
    else:
        print("Incorrecto, intenta de nuevo.")

if __name__ == "__main__":
    verificar_flag()
