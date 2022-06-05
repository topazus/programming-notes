import csv
import pathlib
from pickletools import read_bytes1
from pprint import pprint

import yaml


def read_file():
    file_path = pathlib.Path("/etc/os-release")
    with open(file_path) as f:
        reader = csv.reader(f, delimiter="=")
        os_info = dict(reader)
    print(os_info)
    pprint(os_info)


def read_yaml_files():
    with open("./config.yaml") as f:
        reader = yaml.safe_load(f)
        print(reader)


with open("/proc/cpuinfo") as f:
    reader = f.read()
    print(repr(reader))
read_yaml_files()
