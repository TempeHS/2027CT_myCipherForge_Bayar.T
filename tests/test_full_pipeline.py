"""Full 5-phase encryption pipeline test.

Run from the project root with:  python tests/test_full_pipeline.py
"""

import sys
import os

# Allow importing engine.py from the parent folder
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from engine import encrypt, decrypt

key = {
    "shift": 7,
    "block_size": 5,
    "password": "SECRETKEY",
    "noise_interval": 4,
    "noise_char": "$",
}

test_messages = [
    "Hello World!",
    "The quick brown fox jumps over the lazy dog.",
    "CipherForge 2026 - Encryption Complete!",
    "abc123!@#",
    "A",
    "",
]

print("=" * 60)
print("CIPHERFORGE 5-PHASE ENCRYPTION TEST")
print("=" * 60)

all_passed = True
for msg in test_messages:
    encrypted = encrypt(msg, key)
    decrypted = decrypt(encrypted, key)
    passed = msg == decrypted
    status = "PASS" if passed else "FAIL"
    print(f"[{status}] '{msg[:30]}...' -> Match: {passed}")
    if not passed:
        all_passed = False
        print(f"   Got: '{decrypted}'")

print("=" * 60)
if all_passed:
    print("ALL TESTS PASSED! Your 5-phase algorithm is complete!")
else:
    print("Some tests failed. Debug your phases.")
print("=" * 60)
