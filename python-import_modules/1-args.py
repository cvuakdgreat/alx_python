#!/usr/bin/python3
import sys

num_arguments = len(sys.argv) - 1
arguments = sys.argv[1:]

if num_arguments == 0:
    print("0 arguments.")
else:
    print(f"{num_arguments} {'argument' if num_arguments == 1 else 'arguments'}:")
    for index, arg in enumerate(arguments, start=1):
        print(f"{index}: {arg}")

