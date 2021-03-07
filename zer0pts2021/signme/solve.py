from pwn import *
import math

#context.log_level = "DEBUG"

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m



#p = process("./chall_determ")
p = remote("crypto.ctf.zer0pts.com", 10298)

p.recvuntil(":")
payload = "a" * 125
print("send %s as payload"%payload)
p.send(payload)

m = int(p.readline().split()[-1], 16)
pub = p.readline()
n, e = int(pub.split()[2][1:-1], 16), int(pub.split()[3][:-1], 16)
sig = int(p.readline().split()[2], 16)

# vuln -> dup in qi & sp
qi = sig

print("n,e : %x, %x"%(n,e))
print("m : %x"%m)
print("sig : %x"%sig)

p_ = math.gcd(pow(pow(sig, e, n) - m,1,n),n)
q_ = n // p_
assert(p_ * q_ == n)
phi = (p_ - 1) * (q_ - 1)
d = modinv(e, phi)

chal = int(p.recvline().split()[3],16)
sig_ = pow(chal, d, n)

p.sendline(hex(sig_)[2:])

p.interactive()
