#INPUT_FILE = 'ciphertext'
#INPUT_FILE = 'testcipher'
INPUT_FILE = 'ciphertext2'
MOD = 40

LOOKUP_1 = "\n \"#()*+/1:=[]abcdefghijklmnopqrstuvwxyz"
LOOKUP_2 = "ABCDEFGHIJKLMNOPQRSTabcdefghijklmnopqrst"

# Read in the ciphertext
with open(INPUT_FILE, 'r') as file:
    ciphertext = file.read()

out = ""
prev = 0
for char in ciphertext:
    lookup2_index = LOOKUP_2.index(char)
    #print(lookup2_index)

    # cur_minus_prev = extended_gcd(lookup2_index, MOD)[1] % MOD
    # print(cur_minus_prev)

    # lookup2_index = (cur - prev) % 40
    # lookup2_index + N * 40 = cur - prev
    # lookup2_index + N * 40 + prev = cur

    cur_index = (lookup2_index + prev) % MOD
    #print(cur_index)

    out += LOOKUP_1[cur_index]
    #print(out)

    prev = cur_index

print(out)