import rwpm	
import sys
import os
from time import sleep
from ctypes import * 
import multiprocessing

def read_int(p,a,s=8,bo=sys.byteorder):
	r = rwpm.process_vm_readv(p,a,s)
	return int.from_bytes(r,byteorder=bo,signed=False)

def write_int(p,a,i,s=8,bo=sys.byteorder):
	if not isinstance(i, (bytes, bytearray)):
		i = i.to_bytes(s, bo)
	r = rwpm.process_vm_writev(p,a,i)
	return r

addy = multiprocessing.Value("L",0)
child_run = multiprocessing.Value("i",True)

pid = os.fork()

if pid: #PARENT PROCESS
	print("Parent process PID:",os.getpid(),"Child process PID:",pid)
	if addy.value == 0:
		sleep(2)
	print("[Parent] Reading int from child memory at %s -> int = %i" % (hex(addy.value),read_int(pid,addy.value)))
	print("[Parent] Writing new int value: ",8)
	write_int(pid,addy.value,8)
	print("[Parent] Reading int from child memory at %s -> int = %i" % (hex(addy.value),read_int(pid,addy.value)))
	child_run.value = False
 

else: #CHILD PROCESS
	x = c_uint(10)
	addy.value = addressof(x)
	while child_run.value:
		print("[Child] current int(x) = %i " % (x.value))
		sleep(1)
	print("[Child] final int(x) = %i " % (x.value))
	os._exit(0)
	





"""
import os 
def parentchild(cwrites): 
   r, w = os.pipe() 
   pid = os.fork() 
   if pid: 
      os.close(w) 
      r = os.fdopen(r) 
      print ("Parent is reading") 
      str = r.read() 
      print( "Parent reads =", str) 
   else: 
      os.close(r) 
      w = os.fdopen (w, 'w') 
      print ("Child is writing") 
      w.write(cwrites) 
      print("Child writes = ",cwrites) 
      w.close() 
# Driver code         
cwrites = "Python Program"
parentchild(cwrites) 
"""
"""
PID = 591043
addr = 0x7fdd42efa710

print(rwpm.process_vm_readv(PID,addr,4))
print(read_int(PID,addr))
"""

