# 🔐 CipherForge

A 5-phase encryption algorithm built from scratch in Python.

## 📋 Description

CipherForge is an educational encryption system that demonstrates how real-world encryption algorithms like AES work. It applies 5 layers of transformation to convert plaintext into unreadable ciphertext.

## ✨ Features

- **5-phase encryption pipeline**
- **Web interface** for easy encryption/decryption
- **Key-based security** with trillions of combinations
- **Automated test suite** for verification

## 🔧 The 5 Phases

| Phase | Name            | Description                             |
| ----- | --------------- | --------------------------------------- |
| 1     | Substitution    | Shifts all characters by a fixed amount |
| 2     | Transposition   | Reverses characters in blocks           |
| 3     | Key-Dependent   | Uses password for variable shifting     |
| 4     | Noise Injection | Adds decoy characters                   |
| 5     | Kerbeus         | Reverses the entire message             |

## 🚀 Getting Started

### Run in Codespaces

1. Click **Code** → **Codespaces** → **Create codespace**
2. Wait for environment to load
3. Run: `python app.py`
4. Open the Ports tab and click the globe icon for port 5000

### Run Tests

```bash
python test_engine.py
```

## 🔑 Key Format

The encryption key is a dictionary with these fields:

```python
key = {
    "shift": 5,              # Phase 1: shift amount (1-94)
    "block_size": 4,         # Phase 2: block size (2-20)
    "password": "SECRET",    # Phase 3: encryption password
    "noise_interval": 3,     # Phase 4: insert noise every N chars
    "noise_char": "~"        # Phase 4: noise character to insert
}
```

## 📊 Security Analysis

### Strengths

- Multi-layer encryption defeats simple attacks
- Password-based encryption provides large key space
- Noise injection defeats frequency analysis

### Weaknesses (Educational Context)

- Not mathematically proven like AES
- Smaller key space than production encryption
- Vulnerable to known-plaintext attacks with enough samples

## 📝 License

MIT License - see [LICENSE](LICENSE) file

## 👤 Author

Munkhbayar Tsogtulga - Tempe High School - 2026

---

_Built as part of Year 9 Digital Technologies_
