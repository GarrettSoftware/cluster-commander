import sys
import test

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
if __name__ == "__main__":
    util.set_testing()
    ipmi.read_etc("ipmi.txt")

    test_main()
    test_pipmi()

