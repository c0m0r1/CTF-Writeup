from pwn import *

context.log_level = "ERROR"

def do(payload):
    p = process("./stub")
    p.recvline()
    p.sendline(payload)
    p.recvline()
    try:
        res = int(p.recvline())
    except:
        res = 0
    while True:
        ec = p.poll()
        if ec: break
    print("%s : %d %d"%(payload, res, ec))
    p.close()

    
    
if __name__ == "__main__":
    BYTES = 2
    for i in range(256 ** BYTES):
        do(hex(i)[2:].rjust(2 * BYTES, "0"))

