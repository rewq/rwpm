#!/usr/bin/env python3

import rwpm

pid = 517342
addr = 0x52e328
size = 4

r = rwpm.process_vm_readv(pid,addr,4)
p1 = int.from_bytes(r, "little")
print(hex(p1))

r = rwpm.process_vm_readv(pid,p1+0x110,4)
p1 = int.from_bytes(r, "little")
print(p1)
#r = rwpm.process_vm_writev(pid,addr,bytes([0x64,0x0,0x0,0x0]))
#print(r)


"""
#offset-heap 0x52e328-0x052a000=0x4328
p1_offset = 0x52e328#0x052a000+0x1f390
players_offset = 0x8#0x052a000+0x1f390+0x8
health = 0x110
z = 0xC
y = 0x10
x = 0x8
yaw = 0x44
pitch = 0x48
team = 0x348

p1 = read_int(pid,p1_offset)
players_v = read_int(pid,p1_offset+players_offset)


player1 = {"health":read_int(pid,p1+health),


"""