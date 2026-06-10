"""pytest-style tests for CipherForge.

Run with: pytest -v
"""

import pytest
from engine import (
    phase1_encrypt,
    phase1_decrypt,
    phase2_encrypt,
    phase2_decrypt,
    encrypt,
    decrypt,
)


class TestPhase1:
    """Tests for Phase 1: Caesar shift."""

    @pytest.fixture
    def key(self):
        """Standard key for Phase 1 tests."""
        return {"shift": 5}

    def test_encrypt_changes_text(self, key):
        """Encryption should modify the original text."""
        original = "Hello"
        encrypted = phase1_encrypt(original, key)
        assert encrypted != original

    def test_decrypt_reverses_encrypt(self, key):
        """Decryption should restore original text."""
        original = "Hello World"
        encrypted = phase1_encrypt(original, key)
        decrypted = phase1_decrypt(encrypted, key)
        assert decrypted == original

    @pytest.mark.parametrize(
        "text", ["a", "AB", "Hello World!", "123 abc XYZ", "Special: @#$%^&*()"]
    )
    def test_various_inputs(self, key, text):
        """Test with various input strings."""
        encrypted = phase1_encrypt(text, key)
        decrypted = phase1_decrypt(encrypted, key)
        assert decrypted == text
