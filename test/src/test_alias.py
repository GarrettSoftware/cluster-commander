import os
import socket
import sys
import subprocess
import inspect
import test

sys.path.append("../src")
import alias


########################################################################
def test_ensure_name1():

   if not alias.ensure_name1(""):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name1("123"):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name1("1"):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name1("a="):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name1("a[]"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name1("a"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name1("a"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name1("a-_"):
      test.print_pass()
   else:
      test.print_fail()


########################################################################
def test_ensure_name2():

   if not alias.ensure_name2(""):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name2("123"):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name2("1"):
      test.print_pass()
   else:
      test.print_fail()

   if not alias.ensure_name2("a="):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name2("a[]"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name2("a"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name2("a"):
      test.print_pass()
   else:
      test.print_fail()

   if alias.ensure_name2("a-_"):
      test.print_pass()
   else:
      test.print_fail()


########################################################################
def test_unalias():
    test.print_no_test()


########################################################################
if __name__ == "__main__":
   test_ensure_name1()
   test_ensure_name2()
   test_unalias()

