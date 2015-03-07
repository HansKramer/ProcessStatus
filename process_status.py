#! /usr/bin/python
#
# \Author   Hans Kramer
# \Date     March 2015
#

import os

class ProcessStatus:

    def __init__(self):
        pass

    def get_all_pids(self):
        return [int(pid) for pid in os.listdir("/proc") if pid.isdigit()]

    def get_pid_by_cmdline(self, cmd_line):
        for pid in self.get_all_pids():
            try:
                d = open("/proc/%d/cmdline" % pid).readline().split('\0')
                while d[-1] == '':
                    d.pop()
                if d[:len(cmd_line)] == cmd_line:
                    return pid
            except:  # process might have died in the mean time
                pass
        return None

    def get_all_cmdline(self):
        data = {}
        for pid in self.get_all_pids():
            try:
                d = open("/proc/%d/cmdline" % pid).readline().split('\0')
                while d[-1] == '':
                    d.pop()
                data[pid] = d
            except:  # process might have died in the mean time
                pass
        return data
        


if __name__ == "__main__":
    ps = ProcessStatus()
    print ps.get_all_pids() 
    print ps.get_pid_by_cmdline(["/usr/local/bin/memcached"])
    pid = ps.get_pid_by_cmdline(['/usr/bin/python', './process_status.py'])
    print pid
    print ps.get_all_cmdline()
    print ps.get_all_cmdline()[pid]
