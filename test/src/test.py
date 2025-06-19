import inspect

TEST_NAME_WIDTH = 30


########################################################################
def get_testname(extra_info):
    testname = inspect.stack()[2].function
    if extra_info != "":
        testname += f" ({extra_info})"
    testname += ":"
    testname = testname.ljust(TEST_NAME_WIDTH)
    return testname


########################################################################
def print_pass(extra_info=""):
    testname = get_testname(extra_info)
    print(f"{testname} \033[1;32mPass\033[0m")


########################################################################
def print_fail(extra_info=""):
    testname = get_testname(extra_info)
    print(f"{testname} \033[1;31mFail\033[0m")


########################################################################
def print_no_test(extra_info=""):
    testname = get_testname(extra_info)
    print(f"{testname} \033[1;33mNo Test\033[0m")

