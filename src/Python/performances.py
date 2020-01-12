#!/usr/bin/python3
from __future__ import print_function

import os
import subprocess
import sys
import time

try:
    import psutil
except:
    try:
        print("Installing psutil...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "psutil"])
    except Exception as e:
        print("Error : cannot install psutil ({})".format(e))


class logger:
    show_ram_time = False
    process = None
    ram_initial = int(0)
    time_initial = int(0)
    show_debug = False
    def __init__(self, debug = False, show_ram_time = False):
        self.show_ram_time = show_ram_time
        if show_ram_time:
            self.process = psutil.Process(os.getpid())
            self.ram_initial = self.get_ram()
            self.time_initial = int(time.time())
        self.show_debug = debug
        self.debug("Logger initialized")
    def get_ram(self):
        if sys.version[0] == 2:
            self.process = psutil.Process(os.getpid())
            return self.process.memory_info()[0] / float(2**20)
        else:
            self.process = psutil.Process(os.getpid())
            return self.process.memory_info().rss / float(2**20)
    def get_time(self):
        return int(time.time())
    def log(self, message):
        prefix=""
        if self.show_ram_time:
            prefix=str(self.get_time() - self.time_initial) + "s\t" + str(self.get_ram() - self.ram_initial) + "MB\t"
        print(prefix + message  + "          ")
    def progress(self, message):
        prefix=""
        if self.show_ram_time:
            prefix=str(self.get_time() - self.time_initial) + "s\t\t"
        print(prefix + message, end="\r")
    def debug(self, message):
        if self.show_debug:
            prefix=""
            if self.show_ram_time:
                prefix=str(self.get_time() - self.time_initial) + "s\t" + str(self.get_ram() - self.ram_initial) + "MB\t"
            print(prefix + message + "          ")
