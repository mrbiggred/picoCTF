 #!/usr/bin/env python3
 
from pathlib import Path
 
so_path = "four-unzip/lib/x86_64/libhellojni.so"
 
data = Path(so_path).read_bytes()

# In this binary, pepper's encoded bytes start at file offset 0x1aa0
# and are 0x1f bytes long.
pepper_blob = data[0x1AA0:0x1AA0 + 0x1F]

key = b"alphabetsoup"
decoded = bytes(b ^ key[i % len(key)] for i, b in enumerate(pepper_blob))

print("rodata bytes:", pepper_blob)
print("decoded:", decoded.decode())