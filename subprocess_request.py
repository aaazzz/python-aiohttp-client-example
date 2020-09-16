import sys
from subprocess import Popen, PIPE

def main(argv):
    if len(argv) < 2 or not argv[1].isnumeric():
        print('Invalid Arguments')
        return -1

    cmds_list = [['python3', 'call.py'] for i in range(int(argv[1]))]
    procs_list = [Popen(cmd, stdout=None, stderr=None) for cmd in cmds_list]
    for proc in procs_list:
        proc.wait()

    return 0

if __name__ == "__main__":
    main(sys.argv)
