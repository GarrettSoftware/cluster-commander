import test
import os
import filecmp


################################################################################
def test_pcmd():
    # pylint: disable=too-many-branches,too-many-statements

    # Test help
    os.system("../bin/pcmd -h > /tmp/cc.pcmd.help1")
    if filecmp.cmp("/tmp/cc.pcmd.help1", "gold/pcmd_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pcmd --help > /tmp/cc.pcmd.help2")
    if filecmp.cmp("/tmp/cc.pcmd.help2", "gold/pcmd_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pcmd -v > /tmp/cc.pcmd.version1")
    if filecmp.cmp("/tmp/cc.pcmd.version1", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pcmd --version > /tmp/cc.pcmd.version2")
    if filecmp.cmp("/tmp/cc.pcmd.version2", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pcmd wh hostname | sort > /tmp/cc.pcmd.normal1")
    if filecmp.cmp("/tmp/cc.pcmd.normal1", "gold/pcmd_hostname.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test no output
    os.system("../bin/pcmd wh echo '' | sort > /tmp/cc.pcmd.no_output1")
    if filecmp.cmp("/tmp/cc.pcmd.no_output1", "gold/pcmd_no_output.txt"):
        test.print_pass("no output")
    else:
        test.print_fail("no output")


    # Test lots of flags
    flags = "-s -d --nc"
    os.system(f"../bin/pcmd {flags} wh hostname | sort > /tmp/cc.pcmd.flags1")
    if filecmp.cmp("/tmp/cc.pcmd.flags1", "gold/pcmd_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --debug --no-color"
    os.system(f"../bin/pcmd {flags} wh hostname | sort > /tmp/cc.pcmd.flags2")
    if filecmp.cmp("/tmp/cc.pcmd.flags2", "gold/pcmd_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    os.system("../bin/pcmd -t1 wh sleep 3 | sort > /tmp/cc.pcmd.timeout1")
    if filecmp.cmp("/tmp/cc.pcmd.timeout1", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pcmd -t 1 wh sleep 3 | sort > /tmp/cc.pcmd.timeout2")
    if filecmp.cmp("/tmp/cc.pcmd.timeout2", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pcmd --timeout=1 wh sleep 3 | sort > /tmp/cc.pcmd.timeout3")
    if filecmp.cmp("/tmp/cc.pcmd.timeout3", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")


################################################################################
def test_pipmi():
    # pylint: disable=too-many-branches,too-many-statements

    # Test help
    os.system("../bin/pipmi -h > /tmp/cc.pipmi.help1")
    if filecmp.cmp("/tmp/cc.pipmi.help1", "gold/pipmi_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pipmi --help > /tmp/cc.pipmi.help2")
    if filecmp.cmp("/tmp/cc.pipmi.help2", "gold/pipmi_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pipmi -v > /tmp/cc.pipmi.version1")
    if filecmp.cmp("/tmp/cc.pipmi.version1", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pipmi --version > /tmp/cc.pipmi.version2")
    if filecmp.cmp("/tmp/cc.pipmi.version2", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pipmi wh power status | sort > /tmp/cc.pipmi.normal1")
    if filecmp.cmp("/tmp/cc.pipmi.normal1", "gold/pipmi_power.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -d --nc"
    os.system(f"../bin/pipmi {flags} wh power status | sort > /tmp/cc.pipmi.flags1")
    if filecmp.cmp("/tmp/cc.pipmi.flags1", "gold/pipmi_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --debug --no-color"
    os.system(f"../bin/pipmi {flags} wh power status | sort > /tmp/cc.pipmi.flags2")
    if filecmp.cmp("/tmp/cc.pipmi.flags2", "gold/pipmi_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    os.system("../bin/pipmi -t1 wh sensor | sort > /tmp/cc.pipmi.timeout1")
    if filecmp.cmp("/tmp/cc.pipmi.timeout1", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pipmi -t 1 wh sensor | sort > /tmp/cc.pipmi.timeout2")
    if filecmp.cmp("/tmp/cc.pipmi.timeout2", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")

    os.system("../bin/pipmi --timeout=1 wh sensor | sort > /tmp/cc.pipmi.timeout3")
    if filecmp.cmp("/tmp/cc.pipmi.timeout3", "gold/timeout.txt"):
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")


################################################################################
def test_pping():
    # pylint: disable=too-many-branches

    # Test help
    os.system("../bin/pping -h > /tmp/cc.pping.help1")
    if filecmp.cmp("/tmp/cc.pping.help1", "gold/pping_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/pping --help > /tmp/cc.pping.help2")
    if filecmp.cmp("/tmp/cc.pping.help2", "gold/pping_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/pping -v > /tmp/cc.pping.version1")
    if filecmp.cmp("/tmp/cc.pping.version1", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/pping --version > /tmp/cc.pping.version2")
    if filecmp.cmp("/tmp/cc.pping.version2", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/pping wh | sort > /tmp/cc.pping.normal1")
    if filecmp.cmp("/tmp/cc.pping.normal1", "gold/pping.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test bad call
    os.system("../bin/pping wh1 | sort > /tmp/cc.pping.bad1")
    if filecmp.cmp("/tmp/cc.pping.bad1", "gold/pping_badhost.txt"):
        test.print_pass("badhost")
    else:
        test.print_fail("badhost")


    # Test lots of flags
    flags = "-s -d --nc"
    os.system(f"../bin/pping {flags} wh | sort > /tmp/cc.pping.flags1")
    if filecmp.cmp("/tmp/cc.pping.flags1", "gold/pping_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --debug --no-color"
    os.system(f"../bin/pping {flags} wh | sort > /tmp/cc.pping.flags2")
    if filecmp.cmp("/tmp/cc.pping.flags2", "gold/pping_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")


    # Test timeout
    # No good way to test timeout
    test.print_no_test("timeout")


################################################################################
def test_ppower():
    # pylint: disable=too-many-branches

    # Test help
    os.system("../bin/ppower -h > /tmp/cc.ppower.help1")
    if filecmp.cmp("/tmp/cc.ppower.help1", "gold/ppower_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system("../bin/ppower --help > /tmp/cc.ppower.help2")
    if filecmp.cmp("/tmp/cc.ppower.help2", "gold/ppower_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system("../bin/ppower -v > /tmp/cc.ppower.version1")
    if filecmp.cmp("/tmp/cc.ppower.version1", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system("../bin/ppower --version > /tmp/cc.ppower.version2")
    if filecmp.cmp("/tmp/cc.ppower.version2", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test normal call
    os.system("../bin/ppower wh status | sort > /tmp/cc.ppower.normal1")
    if filecmp.cmp("/tmp/cc.ppower.normal1", "gold/ppower_status.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Test lots of flags
    flags = "-s -d --nc"
    os.system(f"../bin/ppower {flags} wh status | sort > /tmp/cc.ppower.flags1")
    if filecmp.cmp("/tmp/cc.ppower.flags1", "gold/ppower_flags.txt"):
        test.print_pass("flags")
    else:
        test.print_fail("flags")

    flags = "--space --debug --no-color"
    os.system(f"../bin/ppower {flags} wh status | sort > /tmp/cc.ppower.flags2")
    if filecmp.cmp("/tmp/cc.ppower.flags2", "gold/ppower_flags.txt"):
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
