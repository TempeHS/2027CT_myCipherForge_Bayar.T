def phase1_encrypt(text, key):
    """
    Phase 1: Substitution — Shift every character by a fixed amount.

    This layer changes WHAT each character is (its identity).

    Args:
        text: The plaintext string to encrypt
        key: Dictionary containing encryption settings

    Returns:
        The encrypted string with all characters shifted
    """
    # Get the shift amount from the key (default to 5 if not specified)
    shift = key.get("shift", 5)

    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:  # Printable ASCII range
            position = ord(char) - 32
            new_position = (position + shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    return result


def phase1_decrypt(text, key):
    """
    Phase 1: Reverse the substitution.

    Decryption shifts in the OPPOSITE direction (subtracts instead of adds).

    Args:
        text: The encrypted string
        key: Dictionary containing the same encryption settings

    Returns:
        The decrypted (original) string
    """
    shift = key.get("shift", 5)

    result = ""
    for char in text:
        if 32 <= ord(char) <= 126:
            position = ord(char) - 32
            new_position = (position - shift) % 95  # SUBTRACT to reverse!
            result += chr(new_position + 32)
        else:
            result += char

    return result


def encrypt(text, key):
    """
    CipherForge Master Encryption — Applies all 5 phases.

    Currently implemented: Phase 1 only
    Coming soon: Phases 2-5

    Args:
        text: The plaintext to encrypt
        key: Dictionary with settings for all phases

    Returns:
        Fully encrypted string
    """
    # Phase 1: Substitution
    result = phase1_encrypt(text, key)

    # TODO: Phase 2 — Transposition
    # result = phase2_encrypt(result, key)

    # TODO: Phase 3 — Key-Dependent
    # result = phase3_encrypt(result, key)

    # TODO: Phase 4 — Noise Injection
    # result = phase4_encrypt(result, key)

    # TODO: Phase 5 — Wild Card
    # result = phase5_encrypt(result, key)

    return result


def decrypt(text, key):
    """
    CipherForge Master Decryption — Reverses all 5 phases.

    IMPORTANT: Phases must be reversed in OPPOSITE order!
    Encrypt: 1 → 2 → 3 → 4 → 5
    Decrypt: 5 → 4 → 3 → 2 → 1

    Args:
        text: The encrypted text
        key: Same key used for encryption

    Returns:
        Original plaintext
    """
    result = text

    # TODO: Phase 5 — Reverse Wild Card (first!)
    # result = phase5_decrypt(result, key)

    # TODO: Phase 4 — Reverse Noise Injection
    # result = phase4_decrypt(result, key)

    # TODO: Phase 3 — Reverse Key-Dependent
    # result = phase3_decrypt(result, key)

    # TODO: Phase 2 — Reverse Transposition
    # result = phase2_decrypt(result, key)

    # Phase 1: Reverse Substitution (last!)
    result = phase1_decrypt(result, key)

    return result
