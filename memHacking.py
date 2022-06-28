from pymem import Pymem
import time

pm = Pymem('League of Legends.exe')

print(pm.process_id)
print(pm.base_address)

for i in range(100):
	time.sleep(1)
	print(pm.read_int(pm.base_address + 0x2FADB80)/10000)