import sys
import test
import os
import filecmp

sys.path.append("../src")
import pipmi
import util
import ipmi


################################################################################
def test_pipmi():

    cmd = util.reset_print_buffer()
    args = {
        "extra" : "sel list"}
    pipmi.pipmi("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd sel list\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
def test_main():

    pipmi.main(["pipmi", "cn001", "sel", "list"])
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd sel list\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
def test_sh():

    os.system("../bin/pipmi -h > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi1.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi --help > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi1.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi -v > /tmp/cluster-commander-test.txt")
    os.system("echo '  Cluster Commander: Version 1.1.0 beta' > /tmp/cluster-commander-test2.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "/tmp/cluster-commander-test2.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi --version > /tmp/cluster-commander-test.txt")
    os.system("echo '  Cluster Commander: Version 1.1.0 beta' > /tmp/cluster-commander-test2.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "/tmp/cluster-commander-test2.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi hn power status | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi3.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi -s -e -c --nc hn power status | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi4.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi --space --error --code --no-color hn power status | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi4.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi -t1 hn sensor | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi5.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi -t 1 hn sensor | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi5.txt"):
        test.print_pass()
    else:
        test.print_fail()


    os.system("../bin/pipmi --timeout=1 hn sensor | sort > /tmp/cluster-commander-test.txt")
    if filecmp.cmp("/tmp/cluster-commander-test.txt", "gold/pipmi5.txt"):
        test.print_pass()
    else:
        test.print_fail()


################################################################################
if __name__ == "__main__":
    util.set_testing()
    ipmi.read_etc("ipmi.txt")

    test_main()
    test_pipmi()
    test_sh()

