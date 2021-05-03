from pwn import *


b1 = 0x00000000 + 0xdead000
b2 = 0x80000000 + 0xbeef000
with open("./base", "wb") as f:
    f.write(p64(b1) + p64(b2))
