"""
Test script for AES-256 implementation
Run this to verify the encryption/decryption works correctly
"""

from aes256 import (
    aes256_encrypt_block,
    aes256_decrypt_block,
    aes256_encrypt_cbc,
    aes256_decrypt_cbc,
    encrypt_password,
    decrypt_password,
    derive_key_from_password
)

def test_block_encryption():
    """Test basic block encryption/decryption"""
    print("Testing AES-256 block encryption...")

    # Test key (32 bytes = 256 bits)
    key = b'01234567890123456789012345678901'

    # Test plaintext (16 bytes = 128 bits)
    plaintext = b'Hello, World!!!!'  # Exactly 16 bytes

    # Encrypt
    ciphertext = aes256_encrypt_block(plaintext, key)
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext.hex()}")

    # Decrypt
    decrypted = aes256_decrypt_block(ciphertext, key)
    print(f"Decrypted:  {decrypted}")

    assert decrypted == plaintext, "Decryption failed!"
    print("[OK] Block encryption test passed!\n")


def test_cbc_mode():
    """Test CBC mode encryption/decryption"""
    print("Testing AES-256 CBC mode...")

    key = b'01234567890123456789012345678901'
    plaintext = b'This is a longer message that needs padding!'

    # Encrypt
    ciphertext, iv = aes256_encrypt_cbc(plaintext, key)
    print(f"Plaintext:  {plaintext}")
    print(f"IV:         {iv.hex()}")
    print(f"Ciphertext: {ciphertext.hex()[:64]}...")

    # Decrypt
    decrypted = aes256_decrypt_cbc(ciphertext, key, iv)
    print(f"Decrypted:  {decrypted}")

    assert decrypted == plaintext, "CBC decryption failed!"
    print("[OK] CBC mode test passed!\n")


def test_password_encryption():
    """Test high-level password encryption"""
    print("Testing password encryption/decryption...")

    master_password = "MySecureMasterPassword123!"
    password = "MySecretPassword"

    # Derive key
    master_key, salt = derive_key_from_password(master_password)
    print(f"Master key derived (length: {len(master_key)} bytes)")

    # Encrypt
    encrypted = encrypt_password(password, master_key)
    print(f"Password:   {password}")
    print(f"Encrypted:  {encrypted[:64]}...")

    # Decrypt
    decrypted = decrypt_password(encrypted, master_key)
    print(f"Decrypted:  {decrypted}")

    assert decrypted == password, "Password decryption failed!"
    print("[OK] Password encryption test passed!\n")


def test_round_trip():
    """Test complete round-trip encryption"""
    print("Testing complete round-trip...")

    master_password = "TestPassword123"
    test_passwords = [
        "short",
        "This is a longer password with spaces!",
        "P@ssw0rd!123",
        "中文密码测试",
        "a" * 100  # Very long password
    ]

    master_key, salt = derive_key_from_password(master_password)

    for pwd in test_passwords:
        encrypted = encrypt_password(pwd, master_key)
        decrypted = decrypt_password(encrypted, master_key)
        assert decrypted == pwd, f"Round-trip failed for: {pwd[:20]}..."
        try:
            print(f"[OK] '{pwd[:30]}...' encrypted and decrypted successfully")
        except UnicodeEncodeError:
            print(f"[OK] Password (length {len(pwd)}) encrypted and decrypted successfully")

    print("\n[OK] All round-trip tests passed!\n")


if __name__ == "__main__":
    print("=" * 60)
    print("AES-256 Implementation Test Suite")
    print("=" * 60 + "\n")

    try:
        test_block_encryption()
        test_cbc_mode()
        test_password_encryption()
        test_round_trip()

        print("=" * 60)
        print("[OK] All tests passed!")
        print("=" * 60)
    except Exception as e:
        print(f"\n[ERROR] Test failed with error: {e}")
        import traceback
        traceback.print_exc()
