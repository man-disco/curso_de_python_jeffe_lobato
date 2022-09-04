import os
import sys


def reinicia_programa():
    python = sys.executable
    os.execl(python, python, *sys.argv)
