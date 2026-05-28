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


def phase2_encrypt(text, key):
    """
    Phase 2: Transposition — Rearrange character positions.

    Uses block reversal: split into blocks and reverse each one.
    This layer changes WHERE each character is (its position).

    Args:
        text: The string to transform (already Phase 1 encrypted)
        key: Dictionary containing encryption settings

    Returns:
        The transposed string with characters rearranged
    """
    # Get block size from key (default to 4 if not specified)
    block_size = key.get("block_size", 4)

    result = ""

    # Process text in chunks of block_size
    for i in range(0, len(text), block_size):
        # Extract this block (might be shorter at the end)
        block = text[i : i + block_size]
        # Reverse the block and add to result
        result += block[::-1]

    return result


def phase2_decrypt(text, key):
    """
    Phase 2: Reverse the transposition.

    For block reversal, decryption is the same as encryption!
    Reversing a reversed block returns the original.

    Args:
        text: The transposed string
        key: Dictionary containing the same encryption settings

    Returns:
        The un-transposed string
    """
    # Block reversal is self-inverting: encrypt == decrypt
    # Reverse twice = original!
    block_size = key.get("block_size", 4)

    result = ""
    for i in range(0, len(text), block_size):
        block = text[i : i + block_size]
        result += block[::-1]

    return result


def phase3_encrypt(text, key):
    """
    Phase 3: Password-Dependent — Variable shifts based on password.

    Each character is shifted by a different amount determined by
    the corresponding character in the repeating password.
    This destroys frequency patterns!

    Args:
        text: The string to transform (already Phase 1+2 encrypted)
        key: Dictionary containing encryption settings

    Returns:
        The password-encrypted string
    """
    # Get password from key (default to "SECRET" if not specified)
    password = key.get("password", "SECRET")

    result = ""

    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            # Get the password character for this position (cycling)
            password_char = password[i % len(password)]
            # Calculate shift from password character
            password_shift = ord(password_char) % 95

            # Apply the shift (same math as Phase 1)
            position = ord(char) - 32
            new_position = (position + password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    return result


def phase3_decrypt(text, key):
    """
    Phase 3: Reverse the password-dependent encryption.

    CRITICAL: Must use the SAME password that was used for encryption!
    Wrong password = garbage output.

    Args:
        text: The encrypted string
        key: Dictionary with the SAME password used for encryption

    Returns:
        The decrypted string (if password is correct)
    """
    password = key.get("password", "SECRET")

    result = ""

    for i, char in enumerate(text):
        if 32 <= ord(char) <= 126:
            # Get same password character for this position
            password_char = password[i % len(password)]
            password_shift = ord(password_char) % 95

            # SUBTRACT the shift to reverse encryption
            position = ord(char) - 32
            new_position = (position - password_shift) % 95
            result += chr(new_position + 32)
        else:
            result += char

    return result


def encrypt(text, key):
    """
    CipherForge Master Encryption — Applies all 5 phases.

    Currently implemented: Phases 1-3
    Coming soon: Phases 4-5
    """
    # Phase 1: Substitution — change WHAT characters are
    result = phase1_encrypt(text, key)

    # Phase 2: Transposition — change WHERE characters are
    result = phase2_encrypt(result, key)

    # Phase 3: Password-Dependent — destroy frequency patterns
    result = phase3_encrypt(result, key)

    # TODO: Phase 4 — Noise Injection
    # result = phase4_encrypt(result, key)

    # TODO: Phase 5 — Wild Card
    # result = phase5_encrypt(result, key)

    return result


def decrypt(text, key):
    """
    CipherForge Master Decryption — Reverses all 5 phases.

    CRITICAL: Phases reversed in OPPOSITE order!
    Encrypt: 1 → 2 → 3 → 4 → 5
    Decrypt: 5 → 4 → 3 → 2 → 1
    """
    result = text

    # TODO: Phase 5 — Reverse Wild Card (first!)
    # result = phase5_decrypt(result, key)

    # TODO: Phase 4 — Reverse Noise Injection
    # result = phase4_decrypt(result, key)

    # Phase 3: Reverse Password-Dependent
    result = phase3_decrypt(result, key)

    # Phase 2: Reverse Transposition
    result = phase2_decrypt(result, key)

    # Phase 1: Reverse Substitution (last!)
    result = phase1_decrypt(result, key)

    return result
