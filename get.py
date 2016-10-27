import os

def getCPUtemperature():
	res = os.popen('vcgencmd measure_temp').readline()
	return(res.replace("temp=","").replace("'C\n",""))

def getCPUuse():
	return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip()))
CPU_temp = getCPUtemperature()
CPU_usage = getCPUuse()

if __name__ == '__main__':
	print('')
	print('CPU Temperature = '+CPU_temp)
	print('CPU use = '+CPU_usage)

