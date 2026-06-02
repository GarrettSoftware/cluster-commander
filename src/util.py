import builtins
import sys
import os
import threading
import signal


TESTING = False
NO_PRINT = threading.Lock()
PRINT_BUFFER = ""


################################################################################
def print(string): # pylint: disable=redefined-builtin
    # pylint: disable=global-statement
    global PRINT_BUFFER

    if not NO_PRINT.locked():
        builtins.print(string)
    else:
        PRINT_BUFFER += string + "\n"


################################################################################
def get_and_reset_print_buffer():
    buf = get_print_buffer()
    reset_print_buffer()
    return buf


################################################################################
def get_print_buffer():
    return PRINT_BUFFER


################################################################################
def reset_print_buffer():
    # pylint: disable=global-statement
    global PRINT_BUFFER
    PRINT_BUFFER = ""


################################################################################
def set_no_print():
    # pylint: disable=global-statement
    global NO_PRINT
    NO_PRINT.acquire()


################################################################################
def set_testing():
    # pylint: disable=global-statement
    global TESTING, NO_PRINT
    TESTING = True
    NO_PRINT.acquire()


################################################################################
def is_testing():
    return TESTING


################################################################################
def get_root_dir():
    root_dir = os.path.dirname(sys.argv[0])
    while True:
        if root_dir == "/":
            print("Error: Internal error - get_root_dir")
            sys.exit(1)
        if not os.path.exists(root_dir + "/version.txt"):
            root_dir = os.path.dirname(root_dir)
        else:
            break

    return root_dir


################################################################################
def catch_ctrl_c():
    signal.signal(signal.SIGINT, ctrl_c_signal)


################################################################################
def ctrl_c_signal(sig, frame): # pylint: disable=unused-argument
    raise KeyboardInterrupt()
