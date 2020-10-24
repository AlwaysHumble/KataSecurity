#Program to stress CPU

import os

print("Running cpu eater")

os.system("stress-ng --vm 1 --timeout 1s")