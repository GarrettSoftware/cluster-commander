import sys
import test

sys.path.append("../src")
import run
import util


################################################################################
def test_run_cmd():

    # Test normal success
    (out, err, code, cmd) = run.run_cmd("echo hello", timeout=10)
    if out == "hello" and err == "" and code == 0 and cmd == "echo hello":
        test.print_pass("success")
    else:
        test.print_fail("success")

    # Test failure
    (out, err, code, cmd) = run.run_cmd("ls asdf", timeout=10)
    if out == "" and err != "" and code != 0 and cmd == "ls asdf":
        test.print_pass("failure")
    else:
        test.print_fail("failure")

    # Test timeout
    (out, err, code, cmd) = run.run_cmd("sleep 10", timeout=1)
    if out == "<timeout: 1s>" and err == "<timeout: 1s>" and code == -1 and cmd == "sleep 10":
        test.print_pass("timeout")
    else:
        test.print_fail("timeout")


################################################################################
def test_print_output():

    args0 = {
        "color" : False,
        "error" : False,
        "code"  : False,
        "debug" : False,
        "space" : False }
    args1 = {
        "color" : True,
        "error" : True,
        "code"  : True,
        "debug" : True,
        "space" : True}

    out = ("stdout", "stderr", 0, "cmd")
    util.reset_print_buffer()

    # Test args all false
    run.print_output("cn001", out, args0)
    output = util.get_and_reset_print_buffer()
    if output == "[cn001]: stdout\n":
        test.print_pass("args false")
    else:
        test.print_fail("args false")

    # Test args all true
    run.print_output("cn001", out, args1)
    output = util.get_and_reset_print_buffer()
    line1 = "\033[1;32m[cn001]\033[0m: stdout\n"
    line2 = "\033[1;31m[STDERR cn001]\033[0m: stderr\n"
    line3 = "\033[1;33m[CODE cn001]\033[0m: 0\n"
    line4 = "\033[1;35m[DEBUG cn001]\033[0m: cmd\n"
    if output == line1 + line2 + line3 + line4 + "\n":
        test.print_pass("args true")
    else:
        test.print_fail("args true")

    # Test args all no color
    args1["color"] = False
    run.print_output("cn001", out, args1)
    output = util.get_and_reset_print_buffer()
    line1 = "[cn001]: stdout\n"
    line2 = "[STDERR cn001]: stderr\n"
    line3 = "[CODE cn001]: 0\n"
    line4 = "[DEBUG cn001]: cmd\n"
    if output == line1 + line2 + line3 + line4 + "\n":
        test.print_pass("no color")
    else:
        test.print_fail("no color")


################################################################################
def test_run_in_parallel():

    node_list_string = "cn001,cn002"
    function = func_for_test_run_in_parallel
    args = ("arg",)
    run.run_in_parallel(node_list_string, function, args)
    output = util.get_and_reset_print_buffer()
    if output == "cn001 arg\ncn002 arg\n" or output == "cn002 arg\ncn001 arg\n":
        test.print_pass()
    else:
        test.print_fail()


################################################################################
def func_for_test_run_in_parallel(node, args):
    util.print(node + " " + args)


################################################################################
if __name__ == "__main__":
    util.set_testing()

    test_run_cmd()
    test_print_output()
    test_run_in_parallel()

