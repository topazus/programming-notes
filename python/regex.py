import re

map = []
with open("/proc/cpuinfo") as f:
    lines = f.readlines()
    for line in lines:
        res = []
        for t in line.split(":"):
            res.append(t.strip())
        print(res)


with open('./spec') as f:
    lines=f.readlines()
    for line in lines:
        if line.startswith('Version'):
            line.write(re.sub('Version:        3.10.0'))