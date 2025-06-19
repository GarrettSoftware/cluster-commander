import test
import os
import filecmp


# Note: cc-test stands for cluster-commander-test

################################################################################
def test_pcmd():

    # Test help
    os.system("../bin/pcmd -h > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pcmd_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pcmd --help > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pcmd_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pcmd -v > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pcmd --version > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pcmd hn hostname | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pcmd_hostname.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -e -c --nc"
    os.system(f"../bin/pcmd {flags} hn hostname | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pcmd_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --error --code --no-color"
    os.system(f"../bin/pcmd {flags} hn hostname | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pcmd_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    os.system("../bin/pcmd -t1 hn sleep 3 | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pcmd -t 1 hn sleep 3 | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pcmd --timeout=1 hn sleep 3 | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")


################################################################################
def test_pipmi():

    # Test help
    os.system("../bin/pipmi -h > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pipmi_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pipmi --help > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pipmi_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pipmi -v > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pipmi --version > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pipmi hn power status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pipmi_power.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -e -c --nc"
    os.system(f"../bin/pipmi {flags} hn power status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pipmi_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --error --code --no-color"
    os.system(f"../bin/pipmi {flags} hn power status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pipmi_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    os.system("../bin/pipmi -t1 hn sensor | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pipmi -t 1 hn sensor | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pipmi --timeout=1 hn sensor | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")


################################################################################
def test_pping():

    # Test help
    os.system("../bin/pping -h > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pping_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pping --help > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pping_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pping -v > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pping --version > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pping hn | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pping.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -e -c --nc"
    os.system(f"../bin/pping {flags} hn | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pping_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --error --code --no-color"
    os.system(f"../bin/pping {flags} hn | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/pping_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    # No good way to test timeout
    test.print_no_test("timeout")


################################################################################
def test_ppower():

    # Test help
    os.system("../bin/ppower -h > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/ppower_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/ppower --help > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/ppower_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/ppower -v > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/ppower --version > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/ppower hn status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/ppower_status.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -e -c --nc"
    os.system(f"../bin/ppower {flags} hn status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/ppower_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --error --code --no-color"
    os.system(f"../bin/ppower {flags} hn status | sort > /tmp/cc-test.txt")
    if filecmp.cmp("/tmp/cc-test.txt", "gold/ppower_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    # No good way to test timeout
    test.print_no_test("timeout")


################################################################################
if __name__ == "__main__":

    print("----- test_pcmd -----")
    test_pcmd()
    print(" ")
    print("----- test_pipmi -----")
    test_pipmi()
    print(" ")
    print("----- test_pping -----")
    test_pping()
    print(" ")
    print("----- test_ppower -----")
    test_ppower()
    print(" ")

