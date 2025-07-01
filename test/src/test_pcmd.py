import sys
import test

sys.path.append("../src")
import pcmd
import util


################################################################################
def test_pcmd():

    args = {"extra" : "hostname"}
    pcmd.pcmd("cn001", args)
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ssh cn001 'hostname'\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
def test_main():

    pcmd.main(["pcmd", "cn001", "hostname"])
    cmd = util.get_and_reset_print_buffer()
    cmd_gold = "ssh cn001 'hostname'\n"
    if cmd == cmd_gold:
        test.print_pass()
    else:
        test.print_fail()


################################################################################
if __name__ == "__main__":
    util.set_testing()
    util.reset_print_buffer()

    test_main()
    test_pcmd()

