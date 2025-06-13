import sys
import util


################################################################################
# Parses all the arguments of: pcmd, pping, pipmi, etc.
#
# Input:
#   argv         - sys.argv
#   description  - Description of program before any other text
#   description2 - Description of program after all text
#
# Return:
#   args         - Returns a dictionary of all argument possibilities, 
#                  the nodelist, and any extra arguments as one string.
################################################################################
def parse(argv, description, description2=""):

    # Default arguments meant for interactive session
    # extra is the parameters after the nodelist
    # Ex: pcmd n1 hostname -s; extra = "hostname -s"
    args = {
        "space" : False,
        "error" : False,
        "code" : False,
        "debug" : False,
        "color" : True,
        "timeout" : None,
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
                print_version()
                sys.exit(0)
            elif arg == '-h' or arg == '--help':
                print_help(description, description2)
                sys.exit(0)
            elif arg == '-s' or arg == '--space':
                args['space'] = True
            elif arg == '-e' or arg == '--error':
                args['error'] = True
            elif arg == '-c' or arg == '--code':
                args['code'] = True
            elif arg == '-d' or arg == '--debug':
                args['debug'] = True
            elif arg == '--nc' or arg == '--no-color':
                args['color'] = False
            elif arg == '-t':
                if len(argv) < i+2:
                    util.print("Error: Timeout flag with no value given")
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

    if args["nodelist"] == "":
        util.print("Error: Nodelist not specified")
        sys.exit(1)

    return args


################################################################################
def parse_timeout(s):
    if len(s) == 0:
        util.print("Error: Could not parse timeout value: '{s}'")
        sys.exit(1)
    if not s.isdigit():
        util.print("Error: Could not parse timeout value: '{s}'")
        sys.exit(1)

    retval = int(s)
    if retval == 0:
        util.print("Error: Timeout cannot be zero")
        sys.exit(1)
    return retval


################################################################################
def print_help(description, description2):
    util.print("")
    for line in description.split("\n"):
        util.print("  " + line)
    util.print("")
    util.print("  OPTIONS:")
    util.print("    -h,   --help              Print this help message")
    util.print("    -v,   --version           Print version")
    util.print("    -s,   --space             Add space between each hosts' output")
    util.print("    -e,   --error             Print standard error")
    util.print("    -c,   --code              Print return code")
    util.print("    -d,   --debug             Print command run by this program")
    util.print("    --nc, --no-color          Do not print in color")
    util.print("    -t,   --timeout=TIMEOUT   Set timeout in seconds (default: None)")
    util.print("")
    util.print("  NODELIST:")
    util.print("    Comma separated list of nodes.  Nodes can use ranges as well.")
    util.print("    Examples:")
    util.print("      node1,node2,node3,node5,node6,node7")
    util.print("      node[1-3],node[5-7]")
    util.print("      node[1-3,5-7]")
    util.print("      node[01-10]")

    if description2 != "":
        util.print("")
        for line in description2.split("\n"):
            util.print("  " + line)

    util.print("")


################################################################################
def print_version():
    path = util.get_root_dir()
    with open(f"{path}/version.txt", "r") as f:
        version = f.read().strip()
    util.print(f"  Cluster Commander: Version {version}")

