import sys
import rwpm
from pgrep import pgrep
import struct

endian = sys.byteorder

is_64bits = sys.maxsize > 2**32

size_ptr = is_64bits*4+4

size_int = is_64bits*4+4

def read_b(p,a,s=4,bo=sys.byteorder,ro=False):
	r = rwpm.process_vm_readv(p,a,s)
	if ro:
		r = bytearray(r)
	return memoryview(r)

def read_int(p,a,s=8,bo=sys.byteorder):
	r = rwpm.process_vm_readv(p,a,s)
	return int.from_bytes(r,byteorder=bo,signed=False)

def write_int(p,a,i,s=8,bo=sys.byteorder):
	if not isinstance(i, (bytes, bytearray)):
		i = i.to_bytes(s, bo)
	r = rwpm.process_vm_writev(p,a,i)
	return r

def write_double(p,a,i,s=8,bo=sys.byteorder):
	if not isinstance(i, (bytes, bytearray)):
		i = struct.pack('d', i)
	r = rwpm.process_vm_writev(p,a,i)
	return r

def read_double(p,a,s=8,bo=sys.byteorder):
	r = rwpm.process_vm_readv(p,a,s)
	return struct.unpack('d', r)[0]

def read_float(p,a,s=4,bo=sys.byteorder):
	r = rwpm.process_vm_readv(p,a,s)
	return struct.unpack('f', r)[0]

def write_float(p,a,i,s=4,bo=sys.byteorder):
	if not isinstance(i, (bytes, bytearray)):
		i = struct.pack('f', i)
	r = rwpm.process_vm_writev(p,a,i)
	return r

addr = 0x55e64d92c010
a_dd = 0x55e64d92c018
size = 4

PID = pgrep('loopy')[0]

#print(read_int(PID,addr))
#print(write_int(PID,addr,101))
#m = read_b(PID,addr,8)
#print(read_double(PID,a_dd))
#f = 4244.54
#print(write_double(PID,a_dd,f))
#print(read_float(PID,0x56550bac0014))
#print(write_float(PID,0x56550bac0014,10.333))