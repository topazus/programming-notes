# read CPU information by reading /proc/cpuinfo file
from typing import List
import re


class CPU(object):
    def __init__(self) -> None:
        self.processor
        self.vendor_id
        self.cpu_family
        self.model
        self.model_name
        self.stepping
        self.microcode
        self.cpu_m_hz
        self.cache_size
        self.physical_id
        self.siblings
        self.core_id
        self.cpu_cores
        self.apicid
        self.initial_apicid
        self.fpu
        self.fpu_exception
        self.cpuid_level
        self.wp
        self.flags
        self.vmx_flags
        self.bugs
        self.bogomips
        self.clflush_size
        self.cache_alignment
        self.address_sizes
        self.power_management


def get_cpuinfo() -> List[CPU]:
    cpus: List[CPU] = []
    cpu: CPU = None
    with open("/proc/cpuinfo") as f:
        for line in f.readlines():
            # () means group
            m = re.match(r"processor\s+: (\d+)", line)
            if m:
                if cpu:
                    cpus.append(cpu)
                cpu = CPU()
                cpu.processor = int(m.group(1))
            m = re.match(r"vendor_id\s+: (.*)", line)
            if m:
                cpu.vendor_id = m.group(1)
            m = re.match(r"physical id\s+: (.*)", line)
            if m:
                cpu.physical_id = int(m.group(1))
            m = re.match(r"siblings\s+: (.*)", line)
            if m:
                cpu.siblings = int(m.group(1))
            m = re.match(r"core id\s+: (.*)", line)
            if m:
                cpu.core_id = int(m.group(1))
            m = re.match(r"cpu cores\s+: (.*)", line)
            if m:
                cpu.cpu_cores = int(m.group(1))
            m = re.match(r"apicid\s+: (.*)", line)
            if m:
                cpu.apicid = int(m.group(1))
    if cpu:
        cpus.append(cpu)
    return cpus
