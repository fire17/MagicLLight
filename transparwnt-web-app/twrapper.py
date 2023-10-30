import subprocess
import time 



command = ['echo', 'this is a test. Does it come out as a single line?']
command = ['python','continues_mic.py']

import subprocess
import sys

command = ['python', 'continues_mic.py']

# Use bufsize=1 to enable line buffering for real-time output
p = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1, universal_newlines=True)

try:
    while True:
        line = p.stdout.readline()
        if not line:
            break  # No more output from the process
        sys.stdout.write(line)  # Print the line immediately
        sys.stdout.flush()  # Flush the output buffer to ensure immediate display
except:
    p.kill()