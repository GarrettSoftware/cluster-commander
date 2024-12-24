import os
import socket
import sys
import subprocess
import inspect
import alias


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
def test_ensure_name1():

   if not alias.ensure_name1(""):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name1("123"):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name1("1"):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name1("a="):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name1("a[]"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name1("a"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name1("a"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name1("a-_"):
      print_pass()
   else:
      print_fail()


########################################################################
def test_ensure_name2():

   if not alias.ensure_name2(""):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name2("123"):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name2("1"):
      print_pass()
   else:
      print_fail()

   if not alias.ensure_name2("a="):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name2("a[]"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name2("a"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name2("a"):
      print_pass()
   else:
      print_fail()

   if alias.ensure_name2("a-_"):
      print_pass()
   else:
      print_fail()


########################################################################
if __name__ == "__main__":
   test_ensure_name1()
   test_ensure_name2()

