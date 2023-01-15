# Currently unused, this is a click-event proof of concept

import select
import sys


def attemptRead():
    f = open("/home/dylan/Documents/Code/dylstatus/file.txt", "a")

    while sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
        line = sys.stdin.readline()
        if line == "[" or line == "[\n":
            line = sys.stdin.readline()
        f.write(line)

    f.close()
