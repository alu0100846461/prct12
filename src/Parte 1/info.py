#! /usr/bin/python
#!encoding: UTF-8

import os
import platform

def hardware ():
    infofile = "/proc/cpuinfo"
    cpuinfo = {}
    if os.path.isfile(infofile):
        f = open(infofile, "r")
        for line in f:
            try:
                name, value = [w.strip() for w in line.split(":")]
            except:
                continue
            if name == "model name":
                cpuinfo["CPU type"] = value
            elif name == "cache size":
                cpuinfo["Cache size"] = value
            elif name == "cpu MHz":
                cpuinfo["CPU speed"] = value + " Hz"
            elif name == "vendor_id":
                cpuinfo["Vendor ID"] = value
        f.close()
    return cpuinfo

def software ():
    soft = {}
    soft["Operative system"] = platform.platform()
    soft["Node"] = platform.uname()[1]
    soft["Python version"] = platform.python_version()
    soft["Python build number"] = platform.python_build()[0]
    soft["Python build date"] = platform.python_build()[1]
    soft["Python compiler"] = platform.python_compiler()
    return soft

if __name__ == "__main__":

    print "\n", hardware(), "\n"
    print software(), "\n"

