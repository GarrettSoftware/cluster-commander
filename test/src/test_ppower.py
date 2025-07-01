import sys
import test

sys.path.append("../src")
import ppower
import util
import ipmi


################################################################################
def test_ppower():

    # Test status
    args = {"extra" : "status"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power status\n"
    if cmd == cmd_gold:
        test.print_pass("status")
    else:
        test.print_fail("status")

    # Test on
    args = {"extra" : "on"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power on\n"
    if cmd == cmd_gold:
        test.print_pass("on")
    else:
        test.print_fail("on")

    # Test off
    args = {"extra" : "off"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power off\n"
    if cmd == cmd_gold:
        test.print_pass("off")
    else:
        test.print_fail("off")

    # Test cycle
    args = {"extra" : "cycle"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power cycle\n"
    if cmd == cmd_gold:
        test.print_pass("cycle")
    else:
        test.print_fail("cycle")

    # Test reset
    args = {"extra" : "reset"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power reset\n"
    if cmd == cmd_gold:
        test.print_pass("reset")
    else:
        test.print_fail("reset")

    # Test soft
    args = {"extra" : "soft"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power soft\n"
    if cmd == cmd_gold:
        test.print_pass("soft")
    else:
        test.print_fail("soft")

    # Test bad command
    args = {"extra" : "statussss"}
    ppower.ppower("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "statussss: command not supported\n"
    if cmd == cmd_gold:
        test.print_pass("bad command")
    else:
        test.print_fail("bad command")


################################################################################
def test_main():

    ppower.main(["ppower", "cn001", "status"])
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ipmitool -C 3 -I lanplus -H cn001-ipmi -U root -P P@ssw0rd power status\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
if __name__ == "__main__":
    util.set_testing()
    util.reset_print_buffer()
    ipmi.read_etc("ipmi.txt")

    test_main()
    test_ppower()

