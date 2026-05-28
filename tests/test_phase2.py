"""Test Phase 2 (block-reversal transposition) encrypt/decrypt.

Run from the project root with:  python tests/test_phase2.py
"""

import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import phase2_encrypt, phase2_decrypt

# Test with block size 4
key = {"block_size": 4}

original = "Hello World!"
print(f"Original: {original}")

encrypted = phase2_encrypt(original, key)
print(f"Encrypted: {encrypted}")

decrypted = phase2_decrypt(encrypted, key)
print(f"Decrypted: {decrypted}")

print(f"Match: {decrypted == original}")

# Try a few different block sizes
for bs in (2, 6):
    k = {"block_size": bs}
    enc = phase2_encrypt("ABCDEFGH", k)
    print(f"block_size={bs}: 'ABCDEFGH' -> '{enc}'")
