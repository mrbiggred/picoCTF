KEY = 22
TEXT_KEY = "trudeau"

cipher = [61578, 109472, 437888, 6842, 0, 20526, 129998, 526834, 478940, 287364, 0, 567886, 143682, 34210, 465256, 0, 150524, 588412, 6842, 424204, 164208, 184734, 41052, 41052, 116314, 41052, 177892, 348942, 218944, 335258, 177892, 47894, 82104, 116314]

# Reverse the encrypt method, not fully decrypted yet.
semi_cipher = [chr(int(char / KEY / 311)) for char in cipher]  
print(semi_cipher)

# Reverse the dynamic_xor_encrypt method
reversed_flag = ""
for i, char in enumerate(semi_cipher):
    print(f"i = {i}")
    print(f"char = {char}")

    key_char = TEXT_KEY[i % len(TEXT_KEY)]
    print(f"keychar = {key_char}")
    
    decrypted_char = chr(ord(char) ^ ord(key_char))
    print(f"decrypted_char = {decrypted_char}")
    
    reversed_flag += decrypted_char

print("\n")

# Reverse the flag:
flag = reversed_flag[::-1]
print(flag)


# Reverse the XOR logic:

# encrypted_char = chr(ord(char) ^ ord(key_char))

# ord(encrypted_char) = ord(char) ^ ord(key_char)
# ord(encrypted_char) ^ ord(key_char) = ord(char)
# chr(ord(encrypted_char) ^ ord(key_char)) = char