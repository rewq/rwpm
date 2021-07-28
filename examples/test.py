#!/usr/bin/env python3

import rwpm

pid = 535058
addr = 0x5570e15dc010
size = 4

r = rwpm.process_vm_readv(pid,addr,4)
print(r)
print(r.hex())

r = rwpm.process_vm_writev(pid,addr,(111).to_bytes(4,'little'))
print(r)
