#!/usr/bin/python3
import sys

# Check if at least one argument is provided
if len(sys.argv) < 2:
    print("Usage: python script_name.py <arguments>")
    sys.exit(1)

# Loop through command-line arguments, excluding the script name
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
