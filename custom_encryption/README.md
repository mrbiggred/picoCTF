
Figured out the that the shared key is 22 since a = 90 and b = 26 means the prime numbers for a is 97 and b is either 29 or 31.

Wrote the test.py file to confirm my hypothosis.  Then taking 61578 reverse enginering it.

```python
def encrypt(plaintext, key):
    cipher = []
    for char in plaintext:
        cipher.append(((ord(char) * key*311)))
    return cipher
```

```
61578 = ord(char) * key * 311
ord(char) = 61578 / (311 * key)
ord(char) = 61578 / (311 * 22)
ord(char) = 9
```

Key of 22 gives a round number.

The next step is to reverse the dynamic_xor_encrypt function which reverses the string and XOR the with the mod of the string "trudeau".

```python
def dynamic_xor_encrypt(plaintext, text_key):
    cipher_text = ""
    key_length = len(text_key)
    for i, char in enumerate(plaintext[::-1]):
        key_char = text_key[i % key_length]
        encrypted_char = chr(ord(char) ^ ord(key_char))
        cipher_text += encrypted_char
    return cipher_text
```

Reverse the XOR logic:

```
encrypted_char = chr(ord(char) ^ ord(key_char))

ord(encrypted_char) = ord(char) ^ ord(key_char)
ord(encrypted_char) ^ ord(key_char) = ord(char)
chr(ord(encrypted_char) ^ ord(key_char)) = char
```

Run (decryption.py)[decryption.py] to decrypt the cipher:

```
python3 decryption.py
```
