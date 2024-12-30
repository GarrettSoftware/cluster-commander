import builtins

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

