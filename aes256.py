"""
AES-256 Implementation from Scratch
Educational implementation of Advanced Encryption Standard (AES-256)

WARNING: This is for educational purposes only. For production use,
always use well-tested libraries like cryptography.fernet or pycryptodome.
"""

import os
import hashlib
from typing import List, Tuple


# AES S-box (Substitution box)
S_BOX = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16
]

# Inverse S-box
INV_S_BOX = [
    0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb,
    0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb,
    0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e,
    0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25,
    0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92,
    0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84,
    0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06,
    0xd0, 0x2c, 0x1e, 0x8f, 0xca, 0x3f, 0x0f, 0x02, 0xc1, 0xaf, 0xbd, 0x03, 0x01, 0x13, 0x8a, 0x6b,
    0x3a, 0x91, 0x11, 0x41, 0x4f, 0x67, 0xdc, 0xea, 0x97, 0xf2, 0xcf, 0xce, 0xf0, 0xb4, 0xe6, 0x73,
    0x96, 0xac, 0x74, 0x22, 0xe7, 0xad, 0x35, 0x85, 0xe2, 0xf9, 0x37, 0xe8, 0x1c, 0x75, 0xdf, 0x6e,
    0x47, 0xf1, 0x1a, 0x71, 0x1d, 0x29, 0xc5, 0x89, 0x6f, 0xb7, 0x62, 0x0e, 0xaa, 0x18, 0xbe, 0x1b,
    0xfc, 0x56, 0x3e, 0x4b, 0xc6, 0xd2, 0x79, 0x20, 0x9a, 0xdb, 0xc0, 0xfe, 0x78, 0xcd, 0x5a, 0xf4,
    0x1f, 0xdd, 0xa8, 0x33, 0x88, 0x07, 0xc7, 0x31, 0xb1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xec, 0x5f,
    0x60, 0x51, 0x7f, 0xa9, 0x19, 0xb5, 0x4a, 0x0d, 0x2d, 0xe5, 0x7a, 0x9f, 0x93, 0xc9, 0x9c, 0xef,
    0xa0, 0xe0, 0x3b, 0x4d, 0xae, 0x2a, 0xf5, 0xb0, 0xc8, 0xeb, 0xbb, 0x3c, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2b, 0x04, 0x7e, 0xba, 0x77, 0xd6, 0x26, 0xe1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0c, 0x7d
]

# Round constants for key expansion
RCON = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1b, 0x36, 0x6c, 0xd8, 0xab, 0x4d, 0x9a]


def galois_multiply(a: int, b: int) -> int:
    """Multiply two numbers in Galois Field GF(2^8)"""
    result = 0
    for i in range(8):
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= 0x11b  # AES irreducible polynomial
        b >>= 1
    return result & 0xff


def sub_bytes(state: List[List[int]], inverse: bool = False) -> List[List[int]]:
    """Substitute bytes using S-box"""
    sbox = INV_S_BOX if inverse else S_BOX
    return [[sbox[state[i][j]] for j in range(4)] for i in range(4)]


def shift_rows(state: List[List[int]], inverse: bool = False) -> List[List[int]]:
    """Shift rows of the state matrix"""
    new_state = [row[:] for row in state]
    if inverse:
        # Inverse shift: rotate right
        new_state[1] = [state[1][3], state[1][0], state[1][1], state[1][2]]
        new_state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
        new_state[3] = [state[3][1], state[3][2], state[3][3], state[3][0]]
    else:
        # Normal shift: rotate left
        new_state[1] = [state[1][1], state[1][2], state[1][3], state[1][0]]
        new_state[2] = [state[2][2], state[2][3], state[2][0], state[2][1]]
        new_state[3] = [state[3][3], state[3][0], state[3][1], state[3][2]]
    return new_state


def mix_columns(state: List[List[int]], inverse: bool = False) -> List[List[int]]:
    """Mix columns using matrix multiplication in GF(2^8)"""
    new_state = [[0 for _ in range(4)] for _ in range(4)]

    if inverse:
        # Inverse mix columns matrix
        matrix = [[0x0e, 0x0b, 0x0d, 0x09],
                  [0x09, 0x0e, 0x0b, 0x0d],
                  [0x0d, 0x09, 0x0e, 0x0b],
                  [0x0b, 0x0d, 0x09, 0x0e]]
    else:
        # Normal mix columns matrix
        matrix = [[0x02, 0x03, 0x01, 0x01],
                  [0x01, 0x02, 0x03, 0x01],
                  [0x01, 0x01, 0x02, 0x03],
                  [0x03, 0x01, 0x01, 0x02]]

    for c in range(4):
        for r in range(4):
            new_state[r][c] = 0
            for i in range(4):
                new_state[r][c] ^= galois_multiply(matrix[r][i], state[i][c])

    return new_state


def add_round_key(state: List[List[int]], round_key: List[List[int]]) -> List[List[int]]:
    """XOR state with round key"""
    return [[state[i][j] ^ round_key[i][j] for j in range(4)] for i in range(4)]


def key_expansion(key: bytes) -> List[List[List[int]]]:
    """Expand 256-bit key into round keys (14 rounds for AES-256)"""
    # Convert key bytes to 8 words (each word is 4 bytes)
    key_words = []
    for i in range(8):
        word = [key[i*4 + j] for j in range(4)]
        key_words.append(word)

    num_rounds = 14
    total_words = 4 * (num_rounds + 1)  # 60 words total for AES-256

    # Generate remaining round keys
    for i in range(8, total_words):
        temp = key_words[i-1][:]

        if i % 8 == 0:
            # Rotate word
            temp = [temp[1], temp[2], temp[3], temp[0]]
            # Substitute bytes
            temp = [S_BOX[b] for b in temp]
            # XOR with round constant
            temp[0] ^= RCON[(i // 8) - 1]
        elif i % 8 == 4:
            # Substitute bytes
            temp = [S_BOX[b] for b in temp]

        # XOR with word 8 positions back
        new_word = [key_words[i-8][j] ^ temp[j] for j in range(4)]
        key_words.append(new_word)

    # Convert to 4x4 matrices for each round (15 round keys total)
    round_key_matrices = []
    for r in range(num_rounds + 1):
        matrix = [[0 for _ in range(4)] for _ in range(4)]
        for i in range(4):
            word_idx = r * 4 + i
            matrix[i] = key_words[word_idx][:]
        round_key_matrices.append(matrix)

    return round_key_matrices


def bytes_to_state(data: bytes) -> List[List[int]]:
    """Convert 16 bytes to 4x4 state matrix (column-major order)"""
    state = [[0 for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            state[j][i] = data[i * 4 + j]
    return state


def state_to_bytes(state: List[List[int]]) -> bytes:
    """Convert 4x4 state matrix to 16 bytes (column-major order)"""
    data = bytearray(16)
    for i in range(4):
        for j in range(4):
            data[i * 4 + j] = state[j][i]
    return bytes(data)


def aes256_encrypt_block(plaintext: bytes, key: bytes) -> bytes:
    """Encrypt a single 16-byte block using AES-256"""
    if len(plaintext) != 16:
        raise ValueError("Plaintext must be exactly 16 bytes")
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes (256 bits)")

    # Expand key
    round_keys = key_expansion(key)

    # Convert plaintext to state
    state = bytes_to_state(plaintext)

    # Initial round: AddRoundKey only
    state = add_round_key(state, round_keys[0])

    # Main rounds (1 to 13)
    for round_num in range(1, 14):
        state = sub_bytes(state, inverse=False)
        state = shift_rows(state, inverse=False)
        state = mix_columns(state, inverse=False)
        state = add_round_key(state, round_keys[round_num])

    # Final round (no MixColumns)
    state = sub_bytes(state, inverse=False)
    state = shift_rows(state, inverse=False)
    state = add_round_key(state, round_keys[14])

    return state_to_bytes(state)


def aes256_decrypt_block(ciphertext: bytes, key: bytes) -> bytes:
    """Decrypt a single 16-byte block using AES-256"""
    if len(ciphertext) != 16:
        raise ValueError("Ciphertext must be exactly 16 bytes")
    if len(key) != 32:
        raise ValueError("Key must be exactly 32 bytes (256 bits)")

    # Expand key
    round_keys = key_expansion(key)

    # Convert ciphertext to state
    state = bytes_to_state(ciphertext)

    # Initial round: AddRoundKey only
    state = add_round_key(state, round_keys[14])

    # Main rounds (13 to 1)
    for round_num in range(13, 0, -1):
        state = shift_rows(state, inverse=True)
        state = sub_bytes(state, inverse=True)
        state = add_round_key(state, round_keys[round_num])
        state = mix_columns(state, inverse=True)

    # Final round (no MixColumns)
    state = shift_rows(state, inverse=True)
    state = sub_bytes(state, inverse=True)
    state = add_round_key(state, round_keys[0])

    return state_to_bytes(state)


def pkcs7_pad(data: bytes, block_size: int = 16) -> bytes:
    """Pad data using PKCS7 padding"""
    padding_length = block_size - (len(data) % block_size)
    padding = bytes([padding_length] * padding_length)
    return data + padding


def pkcs7_unpad(data: bytes) -> bytes:
    """Remove PKCS7 padding"""
    if len(data) == 0:
        raise ValueError("Cannot unpad empty data")
    padding_length = data[-1]
    if padding_length > len(data) or padding_length == 0:
        raise ValueError("Invalid padding")
    return data[:-padding_length]


def derive_key_from_password(password: str, salt: bytes = None) -> Tuple[bytes, bytes]:
    """Derive a 256-bit key from a password using PBKDF2 (SHA-256)"""
    if salt is None:
        salt = os.urandom(16)

    # Use PBKDF2 with SHA-256, 100000 iterations (adjust as needed)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000, dklen=32)
    return key, salt


def aes256_encrypt_cbc(plaintext: bytes, key: bytes, iv: bytes = None) -> Tuple[bytes, bytes]:
    """Encrypt data using AES-256 in CBC mode"""
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes (256 bits)")

    if iv is None:
        iv = os.urandom(16)
    elif len(iv) != 16:
        raise ValueError("IV must be 16 bytes")

    # Pad plaintext
    padded_data = pkcs7_pad(plaintext)

    # Encrypt in CBC mode
    ciphertext = bytearray()
    previous_block = iv

    for i in range(0, len(padded_data), 16):
        block = padded_data[i:i+16]
        # XOR with previous ciphertext block (or IV for first block)
        xor_block = bytes(a ^ b for a, b in zip(block, previous_block))
        encrypted_block = aes256_encrypt_block(xor_block, key)
        ciphertext.extend(encrypted_block)
        previous_block = encrypted_block

    return bytes(ciphertext), iv


def aes256_decrypt_cbc(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """Decrypt data using AES-256 in CBC mode"""
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes (256 bits)")
    if len(iv) != 16:
        raise ValueError("IV must be 16 bytes")
    if len(ciphertext) % 16 != 0:
        raise ValueError("Ciphertext length must be multiple of 16")

    # Decrypt in CBC mode
    plaintext = bytearray()
    previous_block = iv

    for i in range(0, len(ciphertext), 16):
        block = ciphertext[i:i+16]
        decrypted_block = aes256_decrypt_block(block, key)
        # XOR with previous ciphertext block (or IV for first block)
        xor_block = bytes(a ^ b for a, b in zip(decrypted_block, previous_block))
        plaintext.extend(xor_block)
        previous_block = block

    # Remove padding
    return pkcs7_unpad(bytes(plaintext))


# High-level encryption/decryption functions for password manager
def encrypt_password(password: str, master_key: bytes) -> str:
    """Encrypt a password string using AES-256-CBC, returns base64-encoded result"""
    import base64

    # Convert password to bytes
    plaintext = password.encode('utf-8')

    # Encrypt
    ciphertext, iv = aes256_encrypt_cbc(plaintext, master_key)

    # Combine IV and ciphertext, then base64 encode
    combined = iv + ciphertext
    return base64.b64encode(combined).decode('utf-8')


def decrypt_password(encrypted_password: str, master_key: bytes) -> str:
    """Decrypt a base64-encoded password string using AES-256-CBC"""
    import base64

    # Decode from base64
    combined = base64.b64decode(encrypted_password.encode('utf-8'))

    # Extract IV and ciphertext
    iv = combined[:16]
    ciphertext = combined[16:]

    # Decrypt
    plaintext = aes256_decrypt_cbc(ciphertext, master_key, iv)

    return plaintext.decode('utf-8')
