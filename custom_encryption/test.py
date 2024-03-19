
print(ord("p"));

print(len("trudeau"));

def generator(g, x, p):
    return pow(g, x) % p

# u
# 27
# 64
print(generator(29, 90, 97))
print(generator(31, 90, 97))

# v
# 72
# 9
print(generator(29, 26, 97))
print(generator(31, 26, 97))

# key
print(generator(72, 90, 97))
print(generator(9, 90, 97))

# b_key
print(generator(27, 26, 97))
print(generator(64, 26, 97))


# p = 97
# g = 29, 31

# a = 90
# b = 26



