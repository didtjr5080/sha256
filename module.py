from cryptography.fernet import Fernet

def make_key():
    # 키 생성
    key = Fernet.generate_key()

    with open('key', 'wb') as f:
        f.write(key)
        print('키 생성 완료')

def get_key():
    #키 불러오기
    with open('key', 'rb') as f:
        key = f.read()
        key_str = key.decode('utf-8')
        return key_str

def encoding(input_text):
    # 암호화
    cipher = Fernet(get_key())
    plaintext = input_text
    encrypted = cipher.encrypt(plaintext.encode())
    print(f"Encrypted: {encrypted}")
    return encrypted

def denoding(encrypted):
    # 복호화
    cipher = Fernet(get_key())
    decrypted = cipher.decrypt(encrypted).decode()
    print(f"Decrypted: {decrypted}")
    return decrypted
