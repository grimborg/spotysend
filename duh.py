import sys
import re
from subprocess import Popen, PIPE

UNIT_SIZE = {
    'K': 1,
    'M': 1024,
    'G': 1024**2,
    'T': 1024**3,
}

def parse_output(output):
    lines = output.split("\n")
    regex = re.compile("^\s*(\S+)\s+(.*)")
    file_size = dict(reversed(map(regex.findall, lines)))
    return file_size

def get_sizes(args):
    command = " ".join(["du", "-h"] + args)
    process = Popen(command, stdout=PIPE, shell=True)
    output = process.stdout.read()
    lines = output.split("\n")
    regex = re.compile("^\s*(\S+)\s+(.*)")
    pairs = []
    for l in lines:
        f = regex.findall(l)
        if f:
            pairs.append([f[0][1], f[0][0]])
    return pairs

def size_to_kb(size):
    number = float(size[:-1])
    unit = size[-1]
    return number * UNIT_SIZE[unit]

def size_cmp(a, b):
    return cmp(size_to_kb(a[1]), size_to_kb(b[1]))

def size_sort(file_size):
    return sorted(file_size, cmp=size_cmp)

def duh():
    file_sizes = size_sort(get_sizes(sys.argv[1:]))
    for filename, size in file_sizes:
        print size, "\t", filename
    

