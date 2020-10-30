#Program to stress CPU

import os

print("Running cpu eater")

#increase later
os.system("stress --vm 1 --timeout 5s")