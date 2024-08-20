from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# 암호화할 파일 경로
model_path = '3t.onnx'
encrypted_model_path = 'encrypted_3t.onnx'

# 32바이트 길이의 키와 16바이트 길이의 초기화 벡터 생성
key = os.urandom(32)
iv = os.urandom(16)

# AES 암호화 설정
backend = default_backend()
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=backend)
encryptor = cipher.encryptor()

# 패딩 설정 (AES는 블록 단위 암호화이므로 패딩 필요)
padder = padding.PKCS7(algorithms.AES.block_size).padder()

# 파일 읽기 및 암호화
with open(model_path, 'rb') as f:
    data = f.read()

padded_data = padder.update(data) + padder.finalize()
encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

# 암호화된 데이터 저장
with open(encrypted_model_path, 'wb') as f:
    f.write(iv + encrypted_data)

# 키는 안전한 곳에 저장하거나 배포시 포함하지 않음
print(f'Encryption Key: {key.hex()}')
