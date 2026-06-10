# AES-256 Implementation from Scratch

## Overview

This is a **from-scratch implementation** of the Advanced Encryption Standard (AES-256) algorithm. It was created for educational purposes to demonstrate how AES encryption works at a low level.

## ⚠️ Important Security Notice

**This implementation is for educational purposes only.** For production use, always use well-tested, audited cryptographic libraries like:
- `cryptography` (Python)
- `pycryptodome`
- Standard library implementations

Implementing cryptography from scratch is extremely difficult to get right, and even small mistakes can lead to critical security vulnerabilities.

## What Was Implemented

### Core AES-256 Components

1. **S-Box and Inverse S-Box** - Substitution tables for byte transformation
2. **Galois Field Arithmetic** - GF(2^8) multiplication for MixColumns
3. **Key Expansion** - Rijndael key schedule for AES-256 (14 rounds)
4. **AES Operations**:
   - SubBytes (byte substitution)
   - ShiftRows (row rotation)
   - MixColumns (column mixing)
   - AddRoundKey (XOR with round key)
5. **Block Encryption/Decryption** - 16-byte block processing
6. **CBC Mode** - Cipher Block Chaining for encrypting data longer than 16 bytes
7. **PKCS7 Padding** - Standard padding scheme
8. **Key Derivation** - PBKDF2 with SHA-256 for password-based keys

### Integration with FORTRESS

The AES-256 implementation has been integrated into the FORTRESS password manager:

- **Master Password Protection**: Requires a master password to unlock the vault
- **PBKDF2 Key Derivation**: 100,000 iterations of PBKDF2-HMAC-SHA256
- **Salt Storage**: Unique salt per vault stored in `salt.bin`
- **CBC Mode Encryption**: All passwords encrypted using AES-256-CBC
- **Base64 Encoding**: Encrypted data stored as base64 strings in JSON

## File Structure

- `aes256.py` - Complete AES-256 implementation
- `test_aes256.py` - Test suite to verify correctness
- `FORTRESS.py` - Updated password manager using AES-256

## How It Works

### AES-256 Encryption Process

1. **Key Expansion**: 256-bit key → 15 round keys (60 words)
2. **Initial Round**: AddRoundKey only
3. **Main Rounds** (1-13):
   - SubBytes
   - ShiftRows
   - MixColumns
   - AddRoundKey
4. **Final Round** (14):
   - SubBytes
   - ShiftRows
   - AddRoundKey (no MixColumns)

### Decryption Process

Reverse of encryption with inverse operations:
- InvShiftRows
- InvSubBytes
- InvMixColumns (except final round)

### CBC Mode

For data longer than 16 bytes:
1. Pad data to multiple of 16 bytes (PKCS7)
2. Generate random IV (Initialization Vector)
3. Encrypt each block, XORing with previous ciphertext block
4. Store IV with ciphertext

## Usage Example

```python
from aes256 import encrypt_password, decrypt_password, derive_key_from_password

# Derive key from master password
master_key, salt = derive_key_from_password("MyMasterPassword123!")

# Encrypt a password
encrypted = encrypt_password("MySecretPassword", master_key)

# Decrypt the password
decrypted = decrypt_password(encrypted, master_key)
assert decrypted == "MySecretPassword"
```

## Testing

Run the test suite:
```bash
python test_aes256.py
```

Tests verify:
- Block encryption/decryption
- CBC mode with padding
- Password encryption/decryption
- Round-trip encryption for various password types
- Unicode support

## Technical Details

### AES-256 Specifications
- **Key Size**: 256 bits (32 bytes)
- **Block Size**: 128 bits (16 bytes)
- **Number of Rounds**: 14
- **Key Schedule**: 60 words (240 bytes)

### Security Features
- **PBKDF2 Iterations**: 100,000 (configurable)
- **Random IV**: Generated for each encryption
- **Salt**: Unique per vault
- **Base64 Encoding**: Safe storage in JSON

## Comparison with Old Encryption

### Old System (Removed)
- Simple character shifting cipher
- Fixed offsets (5 for username, 1 for password)
- Weak security
- No master password

### New System (AES-256)
- Industry-standard AES-256 encryption
- Master password required
- PBKDF2 key derivation
- CBC mode with random IVs
- Much stronger security

## Limitations & Future Improvements

1. **No Authentication**: Consider adding HMAC for authenticated encryption
2. **No Key Rotation**: Implement key rotation for long-term security
3. **Performance**: Could be optimized (but security > speed)
4. **Error Handling**: Could add more robust error handling
5. **GCM Mode**: Consider AES-GCM for authenticated encryption

## References

- [NIST FIPS 197](https://nvlpubs.nist.gov/nistpubs/fips/nist.fips.197.pdf) - AES Standard
- [Rijndael Algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard)
- [AES Key Schedule](https://en.wikipedia.org/wiki/AES_key_schedule)

## License

Educational use only. Not recommended for production systems.
