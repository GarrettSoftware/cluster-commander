import sys
import os
import my


################################################################################
# Parses all the arguments of: pcmd, pping, pipmi, etc.
#
# Input:
#   argv         - sys.argv
#   prog         - Program name
#   description  - Description of program before any other text
#   description2 - Description of program after all text
#
# Return:
#   args         - Returns a dictionary of all argument possibilities, 
#                  the nodelist, and any extra arguments as one string.
################################################################################
def parse(argv, prog, description, description2=""):

    args = {
        "space" : False,
        "error" : False,
        "code" : False,
        "debug" : False,
        "color" : True,
        "timeout" : 10,
        "nodelist" : "",
        "extra" : ""}

    state = "dashes"
    skip_next_arg = False
    i = 0
    for arg in argv[1:]:

        i = i + 1

        if skip_next_arg:
            skip_next_arg = False
            continue

        if state == "dashes":
            if arg == '-v' or arg == '--version':
                print_version(prog)
                sys.exit(0)
            elif arg == '-h' or arg == '--help':
                print_version(prog)
                print_help(description, description2)
                sys.exit(0)
            elif arg == '-s' or arg == '--print-space':
                args['space'] = True
            elif arg == '-e' or arg == '--print-error':
                args['error'] = True
            elif arg == '-c' or arg == '--print-code':
                args['code'] = True
            elif arg == '-d' or arg == '--print-debug':
                args['debug'] = True
            elif arg == '--nc' or arg == '--no-color':
                args['color'] = False
            elif arg == '-t':
                if len(argv) < i+2:
                    my.print("Error: Timeout flag with no value given")
                    sys.exit(1)
                args['timeout'] = parse_timeout(argv[i+1])
                skip_next_arg = True
            elif arg[0:2] == '-t':
                args['timeout'] = parse_timeout(arg[2:])
            elif arg[0:10] == '--timeout=':
                args['timeout'] = parse_timeout(arg[10:])
            elif arg[0:1] == '-':
                f"Error: Unrecognized argument {args}"
                sys.exit(1)
            else:
                state = "extra"
                args["nodelist"] = arg
        elif state == "extra":
            args["extra"] += arg + " "

    args["extra"] = args["extra"].strip()

    return args


################################################################################
def parse_timeout(s):
    if len(s) == 0:
        sys.exit(1)
    if not s.isdigit():
        sys.exit(1)

    retval = int(s)
    maxint = 1000000000   # 1 billion
    if retval > maxint or retval < 1:
        sys.exit(1)
    return retval


################################################################################
def print_help(description, description2):
    my.print(description)
    my.print("")
    my.print("OPTIONS:")
    my.print("  -h,  --help               Print this help message")
    my.print("  -v,  --version            Print version")
    my.print("  -s,  --space              Add space between hosts")
    my.print("  -e,  --error              Print standard error")
    my.print("  -c,  --code               Print return code")
    my.print("  -d,  --debug              Print command run by this program")
    my.print("  --nc, --no-color          Do not print in color")
    my.print("  -t,   --timeout=TIMEOUT   Set timeout in seconds for commands (default: 10)")
    my.print("")
    my.print("NODELIST:")
    my.print("  Comma separated list of nodes.  Nodes can use ranges as well.")
    my.print("  Examples:")
    my.print("    node1,node2,node3,node5,node6,node7")
    my.print("    node[1-3],node[5-7]")
    my.print("    node[1-3,5-7]")
    my.print("    node[01-10]")

    if description2 != "":
        my.print("")
        my.print(description2)


################################################################################
def print_version(prog):
    path = os.environ["HPC_TOOLS_PATH"]
    os.system(f"echo {prog}: Version $(cat {path}/version.txt)")

