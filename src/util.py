import builtins
import sys
import os


testing = False
print_buffer = ""


################################################################################
def print(s):
    global testing, print_buffer

    if not testing:
        builtins.print(s)
    else:
        print_buffer += s + "\n"


################################################################################
def get_and_reset_print_buffer():
    buffer = get_print_buffer()
    reset_print_buffer()
    return buffer


################################################################################
def get_print_buffer():
    return print_buffer


################################################################################
def reset_print_buffer():
    global print_buffer
    print_buffer = ""


################################################################################
def set_testing():
    global testing
    testing = True


################################################################################
def is_testing():
    return testing


################################################################################
def get_root_dir():
    root_dir = os.path.dirname(sys.argv[0])
    while True:
        if root_dir == "/":
            util.print("Error: Internal error - get_root_dir")
            sys.exit(1)
        if not os.path.exists(root_dir + "/version.txt"):
            root_dir = os.path.dirname(root_dir)
        else:
            break

    return root_dir

