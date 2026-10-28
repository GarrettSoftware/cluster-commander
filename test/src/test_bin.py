import test
import os
import filecmp


################################################################################
def test_common(cmd):
    # pylint: disable=too-many-branches,too-many-statements

    # Test help
    os.system(f"../bin/{cmd} -h > /tmp/cc.{cmd}.help1")
    if filecmp.cmp(f"/tmp/cc.{cmd}.help1", f"gold/{cmd}_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")

    os.system(f"../bin/{cmd} --help > /tmp/cc.{cmd}.help2")
    if filecmp.cmp(f"/tmp/cc.{cmd}.help2", f"gold/{cmd}_help.txt"):
        test.print_pass("help")
    else:
        test.print_fail("help")


    # Test version
    os.system(f"../bin/{cmd} -v > /tmp/cc.{cmd}.version1")
    if filecmp.cmp(f"/tmp/cc.{cmd}.version1", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")

    os.system(f"../bin/{cmd} --version > /tmp/cc.{cmd}.version2")
    if filecmp.cmp(f"/tmp/cc.{cmd}.version2", "gold/version.txt"):
        test.print_pass("version")
    else:
        test.print_fail("version")


    # Test root
    os.system(f"../bin/{cmd} --root > /tmp/cc.{cmd}.root")
    if filecmp.cmp(f"/tmp/cc.{cmd}.root", "gold/root.txt"):
        test.print_pass("root")
    else:
        test.print_fail("root")


    # Test alias
    # Only testing top line so we don't put production machine names
    # in repo
    os.system(f"../bin/{cmd} --alias | head -n 1 > /tmp/cc.{cmd}.alias")
    if filecmp.cmp(f"/tmp/cc.{cmd}.alias", "gold/alias.txt"):
        test.print_pass("alias")
    else:
        test.print_fail("alias")


################################################################################
def test_pcmd():
    # pylint: disable=too-many-branches,too-many-statements

    # Test common flags
    test_common("pcmd")


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
def test_psudo():
    # pylint: disable=too-many-branches,too-many-statements

    # Test common flags
    test_common("psudo")


    # Test normal call
    os.system("../bin/psudo hpcnet,hpcdev hostname | sort > /tmp/cc.psudo.normal1")
    if filecmp.cmp("/tmp/cc.psudo.normal1", "gold/psudo_hostname.txt"):
        test.print_pass("normal")
    else:
        test.print_fail("normal")


    # Only test normal call to save tester on inputting password
    test.print_no_test("no output")
    test.print_no_test("flags")
    test.print_no_test("timeout")


################################################################################
def test_pipmi():
    # pylint: disable=too-many-branches,too-many-statements

    # Test common flags
    test_common("pipmi")


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

    # Test common flags
    test_common("pping")


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

    # Test common flags
    test_common("ppower")


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
    print("----- test_psudo -----")
    test_psudo()
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
