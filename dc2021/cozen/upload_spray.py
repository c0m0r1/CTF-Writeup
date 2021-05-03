from pwn import *
import hashlib

DEBUG = True
LOCAL = True

if LOCAL:
    p = process(["./ld-linux-cozen.so", "./cozen"], env={"LD_LIBRARY_PATH":"./lib-cozen"})
else:
    p = remote("cozen.challenges.ooo", 51015)

if DEBUG:
    context.log_level = "DEBUG"

sla = p.sendlineafter
sl = p.sendline
rl = p.recvline
ru = p.recvuntil

def download(n, down = True):
    sz_max = int(ru("raw bytes").split()[-3])
    print("%s : %d bytes"%(n, sz_max))
    rl()
    sz = 0
    data = ""
    while sz < sz_max:
        tmp = ru("==DONE==")
        sz += len(tmp)
        data += tmp
    data = data[:sz_max]
    md5 = rl().split()[-1]
    h = hashlib.md5()
    h.update(data)
    print(md5, h.hexdigest().upper())
    assert(h.hexdigest().upper() == md5)
    with open(n, "wb") as f:
        f.write(data[:sz_max])

def upload(name, desc, data):
    sla(": ", name)
    sla(": ", desc)
    sla(": ", str(len(data)))
    rl()

    h = hashlib.md5()
    h.update(data)

    p.send(data)
    p.send("==DONE== MD5 ")
    p.send(h.hexdigest())
    sla("exit", "")


sla("[N] ", "N")
sla("[N] ","N")

sla(": ", "".join(random.sample("abcedfghijklmnopqrstuvwxyz1234567890", 5)))
sla("[Y/n]? ","Y")
sla(": ", "c0m0r1")
sla("]: ", "e")
sla("ontinue ","C")

sla(">> ", "F")
sla(">> ", "U")
upload("aaa", "desc", "thisistest")
"""
context.log_level = "ERROR"
sla(">> ", "3")
sla(">> ", "N")
sla(">> ", "N")
sla(">> ", "N")
sla(">> ", "3")
download("libicudata.so.66", False)
context.log_level = "DEBUG"
"""

if LOCAL and DEBUG:
    gdb.attach(p)


p.interactive()

