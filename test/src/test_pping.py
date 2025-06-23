import sys
import test

sys.path.append("../src")
import pping
import util


################################################################################
def test_pping():

    args = None
    pping.pping("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ping -c 1 cn001\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
def test_main():

    pping.main(["pping", "cn001"])
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ping -c 1 cn001\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
if __name__ == "__main__":
    util.set_testing()
    util.reset_print_buffer()

    test_main()
    test_pping()

