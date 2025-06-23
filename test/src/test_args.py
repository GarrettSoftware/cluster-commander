import os
import socket
import sys
import subprocess
import test

sys.path.append("../src")
import args
import util


########################################################################
def test_parse():

    desc1 = "Desc1"
    desc2 = "Desc2"
    arg_default = {
        "space" : False,
        "error" : False,
        "code" : False,
        "debug" : False,
        "color" : True,
        "timeout" : None,
        "nodelist" : "",
        "extra" : ""}

    # Check no nodelist
    try:
        argv = ["command"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass("no nodelist")
        else:
            test.print_fail("no nodelist")

    # Check unrecognized argument
    try:
        argv = ["command", "--not_an_argument", "nodelist"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass("unrecognized arg")
        else:
            test.print_fail("unrecognized arg")

    # Check simplest command (command and nodelist)
    argv = ["command", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    if arg == arg_gold:
        test.print_pass("simple")
    else:
        test.print_fail("simple")

    # Check extra args
    argv = ["command", "nodelist", "hostname", "-s"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["extra"] = "hostname -s"
    if arg == arg_gold:
        test.print_pass("extra args")
    else:
        test.print_fail("extra args")

    # Check simple flags
    argv = ["command", "-s", "-e", "-c", "-d", "--nc", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["space"] = True
    arg_gold["error"] = True
    arg_gold["code"] = True
    arg_gold["debug"] = True
    arg_gold["color"] = False
    if arg == arg_gold:
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    # Check simple long flags
    argv = ["command", "--space", "--error", 
        "--code", "--debug", "--no-color", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["space"] = True
    arg_gold["error"] = True
    arg_gold["code"] = True
    arg_gold["debug"] = True
    arg_gold["color"] = False
    if arg == arg_gold:
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    # Check timeout flag -t10
    argv = ["command", "-t10", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["timeout"] = 10
    if arg == arg_gold:
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    # Check timeout flag -t 10
    argv = ["command", "-t", "10", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["timeout"] = 10
    if arg == arg_gold:
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    # Check timeout flag --timeout=10
    argv = ["command", "--timeout=10", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["timeout"] = 10
    if arg == arg_gold:
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    # Check -v flag
    util.reset_print_buffer()
    try:
        argv = ["command", "-v"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail("version")
    except SystemExit as e:
        version = util.get_and_reset_print_buffer().strip()
        if e.code == 0 and version.startswith("Cluster Commander: Version"):
            test.print_pass("version")
        else:
            test.print_fail("version")

    # Check --version flag
    util.reset_print_buffer()
    try:
        argv = ["command", "--version"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail("version")
    except SystemExit as e:
        version = util.get_and_reset_print_buffer().strip()
        if e.code == 0 and version.startswith("Cluster Commander: Version"):
            test.print_pass("version")
        else:
            test.print_fail("version")

    # Check -h flag
    util.reset_print_buffer()
    try:
        argv = ["command", "-h"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail("help")
    except SystemExit as e:
        help = util.get_and_reset_print_buffer().strip()
        if e.code == 0 and help.startswith("Desc1") and help.endswith("Desc2"):
            test.print_pass("help")
        else:
            test.print_fail("help")

    # Check --help flag
    util.reset_print_buffer()
    try:
        argv = ["command", "--help"]
        arg = args.parse(argv, desc1, desc2)
        arg_gold = arg_default.copy()
        test.print_fail("help")
    except SystemExit as e:
        help = util.get_and_reset_print_buffer().strip()
        if e.code == 0 and help.startswith("Desc1") and help.endswith("Desc2"):
            test.print_pass("help")
        else:
            test.print_fail("help")


########################################################################
def test_print_version():

    util.reset_print_buffer()
    args.print_version()
    version = util.get_and_reset_print_buffer()
    version_gold = "  Cluster Commander: Version 1.1.0 beta\n"

    if version == version_gold:
        test.print_pass()
    else:
        test.print_fail()



########################################################################
def test_print_help():

    help2a = "\n  Description 1\n"
    help3a = "\n  Description 1\n  Description 2\n"

    help2b = "\n"
    help2b += "  OPTIONS:\n"
    help2b += "    -h,   --help              Print this help message\n"
    help2b += "    -v,   --version           Print version\n"
    help2b += "    -s,   --space             Add space between each hosts' output\n"
    help2b += "    -e,   --error             Print standard error\n"
    help2b += "    -c,   --code              Print return code\n"
    help2b += "    -d,   --debug             Print command run by this program\n"
    help2b += "    --nc, --no-color          Do not print in color\n"
    help2b += "    -t,   --timeout=TIMEOUT   Set timeout in seconds (default: None)\n"
    help2b += "\n"
    help2b += "  NODELIST:\n"
    help2b += "    Comma separated list of nodes.  Nodes can use ranges as well.\n"
    help2b += "    Examples:\n"
    help2b += "      node1,node2,node3,node5,node6,node7\n"
    help2b += "      node[1-3],node[5-7]\n"
    help2b += "      node[1-3,5-7]\n"
    help2b += "      node[01-10]\n"
    help2b += "\n"

    help2c = "  Description 2\n\n"
    help3c = "  Description 3\n  Description 4\n\n"

    # Test single line description 1, no description 2
    args.print_help("Description 1", "")
    help1 = util.get_and_reset_print_buffer()
    if help1 == help2a + help2b:
        test.print_pass()
    else:
        test.print_fail()

    # Test multi line description 1, no description 2
    args.print_help("Description 1\nDescription 2", "")
    help1 = util.get_and_reset_print_buffer()
    if help1 == help3a + help2b:
        test.print_pass()
    else:
        test.print_fail()

    # Test single line description 1, single line description 2
    args.print_help("Description 1", "Description 2")
    help1 = util.get_and_reset_print_buffer()
    if help1 == help2a + help2b + help2c:
        test.print_pass()
    else:
        test.print_fail()

    # Test multi line description 1, multi line description 2
    args.print_help("Description 1\nDescription 2", "Description 3\nDescription 4")
    help1 = util.get_and_reset_print_buffer()
    if help1 == help3a + help2b + help3c:
        test.print_pass()
    else:
        test.print_fail()


########################################################################
def test_parse_timeout():

    # Test 0 length string
    try:
        args.parse_timeout("")
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test not digits
    try:
        args.parse_timeout("a")
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test not digits
    try:
        args.parse_timeout("01234a")
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test zero
    try:
        args.parse_timeout("0")
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test zero
    try:
        args.parse_timeout("00000")
        test.print_fail()
    except SystemExit as e:
        if e.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test good numbers
    if args.parse_timeout("1") == 1:
        test.print_pass()
    else:
        test.print_fail()

    # Test good numbers
    if args.parse_timeout("01") == 1:
        test.print_pass()
    else:
        test.print_fail()

    # Test good numbers
    if args.parse_timeout("1000") == 1000:
        test.print_pass()
    else:
        test.print_fail()


########################################################################
if __name__ == "__main__":

    util.set_testing()

    test_parse()
    test_print_version()
    test_print_help()
    test_parse_timeout()

