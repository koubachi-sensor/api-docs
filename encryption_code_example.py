import os
import struct
from zlib import crc32
from Crypto.Cipher import AES

IV_LEN = 16
BLOCK_SIZE = 16
CRC_LEN = 4


def decrypt(key, data):
    # check length
    if len(data) < IV_LEN + BLOCK_SIZE or (len(data) - IV_LEN) % BLOCK_SIZE != 0:
        raise ValueError("invalid data size")
    iv, ciphertext = data[:IV_LEN], data[IV_LEN:]

    # decrypt
    decrypter = AES.new(key, AES.MODE_CBC, iv)
    plaintext = decrypter.decrypt(ciphertext)

    # check crc
    plaintext, crc = plaintext[:-CRC_LEN], plaintext[-CRC_LEN:]
    crc = struct.unpack('>I', crc)[0]
    if crc != crc32(plaintext):
        raise ValueError("invalid checksum")

    # trim padding
    plaintext = plaintext.rstrip(b'\0')

    return plaintext


def encrypt(key, data):
    # add padding
    plaintext = data + bytes(BLOCK_SIZE - (len(data) + CRC_LEN - 1) % BLOCK_SIZE - 1)

    # add crc
    plaintext += struct.pack('>I', crc32(plaintext))

    # random iv
    iv = os.urandom(IV_LEN)

    # encrypt
    encrypter = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = encrypter.encrypt(plaintext)

    return iv + ciphertext


def test_decryption():
    key = bytes.fromhex("00112233445566778899aabbccddeeff")
    data = bytes.fromhex("6cc6527f1d3d56c79d6b130beb76fe90cf170663be65a0952fc3ec7c280a8512"
                         "c989288a55d64514663c85725aff0224633301b7c48bc9d1d14b8b77c77c9920")
    plaintext = decrypt(key, data)
    assert plaintext == b"just some random boring test data"


def test_encryption_and_decryption():
    key = bytes.fromhex("0123456789abcdef0123456789abcdef")
    data = b"another chunk of boring test data for encryption, long enough to fill multiple blocks"
    encrypted = encrypt(key, data)
    decrypted = decrypt(key, encrypted)
    assert decrypted == data
