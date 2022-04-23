from bcc import BPF

x = 4
print hex(id(x))

if x == hex(id(x)):
    print True