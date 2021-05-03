from pwn import *
import hashlib

#context.log_level = "DEBUG"
p = remote("cozen.challenges.ooo", 51015)

sla = p.sendlineafter
sl = p.sendline
rl = p.recvline
ru = p.recvuntil

def download(n):
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

sla("[N] ", "N")
sla("[N] ","N")

sla(": ", "".join(random.sample("abcedfghijklmnopqrstuvwxyz1234567890", 5)))
sla("[Y/n]? ","Y")
sla(": ", "c0m0r1")
sla("]: ", "e")
sla("ontinue ","C")

sla(">> ", "F")
#sla(">> ", "3")
sla(">> ", "6")
download("cozen")
sla(">> ", "7")
download("ld-linux-cozen.so")

sla(">> ", "3")
sla(">> ", "1")
download("libBBSAnnouncements.so")
sla(">> ", "2")
download("libBBSFiles.so")
sla(">> ", "3")
download("libBBSGlobalStats.so")
sla(">> ", "4")
download("libBBSLogin.so")
sla(">> ", "5")
download("libBBSMain.so")
sla(">> ", "6")
download("libBBSMenu.so")
sla(">> ", "7")
download("libBBSMessages.so")
sla(">> ", "8")
download("libBBSRender.so")
sla(">> ", "9")
download("libBBSStats.so")


sla(">> ", "N")
sla(">> ", "1")
download("libBBSSysop.so")
sla(">> ", "2")
download("libBBSUser.so")
sla(">> ", "3")
download("libBBSUserEdit.so")
sla(">> ", "4")
download("libBBSUserSearch.so")
sla(">> ", "5")
download("libBBSUtils.so")
sla(">> ", "6")
download("libBBSWelcome.so")
sla(">> ", "7")
download("libCompressionBase.so")
sla(">> ", "8")
download("libConnectionBase.so")
sla(">> ", "9")
download("libDiffieHellman.so")

sla(">> ", "N")
sla(">> ", "1")
download("libEncryptionBase.so")
sla(">> ", "2")
download("libHashBase.so")
sla(">> ", "3")
download("libSerpent.so")
sla(">> ", "4")
download("libTwofish.so")
sla(">> ", "5")
download("libZLib.so")
sla(">> ", "6")
download("libbsd.so.0")
sla(">> ", "7")
download("libc.so.6")
sla(">> ", "8")
download("libcrc32.so")
sla(">> ", "9")
download("libcrypto.so.1.1")

sla(">> ", "N")
sla(">> ", "1")
download("libdl.so.2")
sla(">> ", "2")
download("libgcc_s.so.1")
sla(">> ", "3")
download("libicudata.so.66")
sla(">> ", "4")
download("libicuuc.so.66")
sla(">> ", "5")
download("liblz77.so")
sla(">> ", "6")
download("libm.so.6")
sla(">> ", "7")
download("libmd5.so")
sla(">> ", "8")
download("libpthread.so.0")
sla(">> ", "9")
download("libssl.so.1.1")

sla(">> ", "N")
sla(">> ", "1")
download("libstdc++.so.6")
sla(">> ", "2")
download("libz.so.1")

sla(">> ", "B")
sla(">> ", "5")
sla(">> ", "1")
download("QEDIT.ZIP")
sla(">> ", "2")
download("WASM211.ZIP")


p.interactive()

