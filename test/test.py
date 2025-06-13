import inspect


########################################################################
def print_pass(testname=None):
   if testname == None:
      testname = inspect.stack()[1].function
   print(f"{testname}: \033[1;32mPass\033[0m")


########################################################################
def print_fail(testname=""):
   testname = inspect.stack()[1].function
   print(f"{testname}: \033[1;31mFail\033[0m")


########################################################################
def print_no_test(testname=""):
   testname = inspect.stack()[1].function
   print(f"{testname}: \033[1;33mNo Test\033[0m")


