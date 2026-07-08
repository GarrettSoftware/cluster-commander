# pylint: disable=no-member
import sys
import test

sys.path.append("../src")
import args # pylint: disable=import-error,wrong-import-position
import util # pylint: disable=import-error,wrong-import-position


########################################################################
def test_parse():
    # pylint: disable=too-many-branches,too-many-statements

    desc1 = "Desc1"
    desc2 = "Desc2"
    arg_default = {
        "space" : False,
        "debug" : False,
        "color" : True,
        "timeout" : None,
        "nodelist" : "",
        "exnodelist" : "",
        "extra" : ""}

    # Check no nodelist
    try:
        argv = ["command"]
        arg = args.parse(argv, desc1, desc2)
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
            test.print_pass("no nodelist")
        else:
            test.print_fail("no nodelist")

    # Check unrecognized argument
    try:
        argv = ["command", "--not_an_argument", "nodelist"]
        arg = args.parse(argv, desc1, desc2)
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
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
    argv = ["command", "-s", "-d", "--nc", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["space"] = True
    arg_gold["debug"] = True
    arg_gold["color"] = False
    if arg == arg_gold:
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    # Check simple long flags
    argv = ["command", "--space", "--debug", "--no-color", "nodelist"]
    arg = args.parse(argv, desc1, desc2)
    arg_gold = arg_default.copy()
    arg_gold["nodelist"] = "nodelist"
    arg_gold["space"] = True
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
        test.print_fail("version")
    except SystemExit as exc:
        version = util.get_and_reset_print_buffer().strip()
        if exc.code == 0 and version.startswith("Cluster Commander: Version"):
            test.print_pass("version")
        else:
            test.print_fail("version")

    # Check --version flag
    util.reset_print_buffer()
    try:
        argv = ["command", "--version"]
        arg = args.parse(argv, desc1, desc2)
        test.print_fail("version")
    except SystemExit as exc:
        version = util.get_and_reset_print_buffer().strip()
        if exc.code == 0 and version.startswith("Cluster Commander: Version"):
            test.print_pass("version")
        else:
            test.print_fail("version")

    # Check -h flag
    util.reset_print_buffer()
    try:
        argv = ["command", "-h"]
        arg = args.parse(argv, desc1, desc2)
        test.print_fail("help")
    except SystemExit as exc:
        help1 = util.get_and_reset_print_buffer().strip()
        if exc.code == 0 and help1.startswith("Desc1") and help1.endswith("Desc2"):
            test.print_pass("help")
        else:
            test.print_fail("help")

    # Check --help flag
    util.reset_print_buffer()
    try:
        argv = ["command", "--help"]
        arg = args.parse(argv, desc1, desc2)
        test.print_fail("help")
    except SystemExit as exc:
        help1 = util.get_and_reset_print_buffer().strip()
        if exc.code == 0 and help1.startswith("Desc1") and help1.endswith("Desc2"):
            test.print_pass("help")
        else:
            test.print_fail("help")


########################################################################
def test_print_version():

    util.reset_print_buffer()
    args.print_version()
    version = util.get_and_reset_print_buffer()
    version_gold = "  Cluster Commander: Version 1.3.0\n"

    if version == version_gold:
        test.print_pass()
    else:
        test.print_fail()


########################################################################
def test_print_help():
    test.print_no_test("Tested with test_bin.sh")


########################################################################
def test_parse_timeout():
    # pylint: disable=too-many-branches,too-many-statements

    # Test 0 length string
    try:
        args.parse_timeout("")
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test not digits
    try:
        args.parse_timeout("a")
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test not digits
    try:
        args.parse_timeout("01234a")
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test zero
    try:
        args.parse_timeout("0")
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
            test.print_pass()
        else:
            test.print_fail()

    # Test zero
    try:
        args.parse_timeout("00000")
        test.print_fail()
    except SystemExit as exc:
        if exc.code == 1:
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
