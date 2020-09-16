from subprocess import Popen, PIPE

cmds_list = [['python3', 'call.py'] for i in range(10)]
procs_list = [Popen(cmd, stdout=PIPE, stderr=PIPE) for cmd in cmds_list]
for proc in procs_list:
	proc.wait()
