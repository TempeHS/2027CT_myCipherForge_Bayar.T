"""Test Phase 1 (substitution) encrypt/decrypt.

Run from the project root with:  python tests/test_phase1.py
"""

import sys
import os

# Allow importing engine.py from the parent folder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase1_encrypt, phase1_decrypt

# Create a key with shift value 7
key = {"shift": 7}

# Test encryption
message = "Hello CipherForge!"
encrypted = phase1_encrypt(message, key)
print(f"Encrypted: {encrypted}")

# Test decryption
decrypted = phase1_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

# Verify reversibility
print(f"Match: {decrypted == message}")

# Try a few different shift values
for shift in (1, 13, 50):
    k = {"shift": shift}
    sample = "Attack at dawn!"
    enc = phase1_encrypt(sample, k)
    dec = phase1_decrypt(enc, k)
    print(f"shift={shift}: enc='{enc}' dec_match={dec == sample}")
