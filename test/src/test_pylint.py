import sys
import test

sys.path.append("../src")
import run # pylint: disable=import-error,wrong-import-position


################################################################################
def test_pylint():
    # pylint: disable=too-many-branches,too-many-statements

    success_string = "Your code has been rated at 10.00/10"

    (out, _, _, _) = run.run_cmd("pylint src/test_alias.py", timeout=10)
    if success_string in out:
        test.print_pass("test_alias.py")
    else:
        test.print_fail("test_alias.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_args.py", timeout=10)
    if success_string in out:
        test.print_pass("test_args.py")
    else:
        test.print_fail("test_args.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_bin.py", timeout=10)
    if success_string in out:
        test.print_pass("test_bin.py")
    else:
        test.print_fail("test_bin.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_ipmi.py", timeout=10)
    if success_string in out:
        test.print_pass("test_ipmi.py")
    else:
        test.print_fail("test_ipmi.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_parse.py", timeout=10)
    if success_string in out:
        test.print_pass("test_parse.py")
    else:
        test.print_fail("test_parse.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_pcmd.py", timeout=10)
    if success_string in out:
        test.print_pass("test_pcmd.py")
    else:
        test.print_fail("test_pcmd.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_pipmi.py", timeout=10)
    if success_string in out:
        test.print_pass("test_pipmi.py")
    else:
        test.print_fail("test_pipmi.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_pping.py", timeout=10)
    if success_string in out:
        test.print_pass("test_pping.py")
    else:
        test.print_fail("test_pping.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_ppower.py", timeout=10)
    if success_string in out:
        test.print_pass("test_ppower.py")
    else:
        test.print_fail("test_ppower.py")

    (out, _, _, _) = run.run_cmd("pylint src/test.py", timeout=10)
    if success_string in out:
        test.print_pass("test.py")
    else:
        test.print_fail("test.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_pylint.py", timeout=10)
    if success_string in out:
        test.print_pass("test_pylint.py")
    else:
        test.print_fail("test_pylint.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_run.py", timeout=10)
    if success_string in out:
        test.print_pass("test_run.py")
    else:
        test.print_fail("test_run.py")

    (out, _, _, _) = run.run_cmd("pylint src/test_util.py", timeout=10)
    if success_string in out:
        test.print_pass("test_util.py")
    else:
        test.print_fail("test_util.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/alias.py", timeout=10)
    if success_string in out:
        test.print_pass("alias.py")
    else:
        test.print_fail("alias.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/args.py", timeout=10)
    if success_string in out:
        test.print_pass("args.py")
    else:
        test.print_fail("args.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/ipmi.py", timeout=10)
    if success_string in out:
        test.print_pass("ipmi.py")
    else:
        test.print_fail("ipmi.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/parse.py", timeout=10)
    if success_string in out:
        test.print_pass("parse.py")
    else:
        test.print_fail("parse.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/pcmd.py", timeout=10)
    if success_string in out:
        test.print_pass("pcmd.py")
    else:
        test.print_fail("pcmd.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/pipmi.py", timeout=10)
    if success_string in out:
        test.print_pass("pipmi.py")
    else:
        test.print_fail("pipmi.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/pping.py", timeout=10)
    if success_string in out:
        test.print_pass("pping.py")
    else:
        test.print_fail("pping.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/ppower.py", timeout=10)
    if success_string in out:
        test.print_pass("ppower.py")
    else:
        test.print_fail("ppower.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/run.py", timeout=10)
    if success_string in out:
        test.print_pass("run.py")
    else:
        test.print_fail("run.py")

    (out, _, _, _) = run.run_cmd("pylint ../src/util.py", timeout=10)
    if success_string in out:
        test.print_pass("util.py")
    else:
        test.print_fail("util.py")


################################################################################
if __name__ == "__main__":
    test_pylint()
