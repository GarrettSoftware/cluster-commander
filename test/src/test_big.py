import inspect
import misc


########################################################################
def print_pass():
   testname = inspect.stack()[1].function
   print(f"{testname}: \033[1;32mPass\033[0m")


########################################################################
def print_fail():
   testname = inspect.stack()[1].function
   print(f"{testname}: \033[1;31mFail\033[0m")


########################################################################
def test_pcmd():
   try:
      (out,err,code) = misc.run_cmd("pcmd wh[001-003] hostname")
   except:
      print("test_pcmd exception!")
      print_fail()
      return
   if code == 0:
      print_pass()
   else:
      print_fail()
   print("--- pcmd out ---")
   print(out)
   if err != "":
      print("--- pcmd err ---")
      print(err)
   if code != 0:
      print("--- pcmd code ---")
      print(code)


########################################################################
def test_pipmi():
   try:
      (out,err,code) = misc.run_cmd("pipmi wh[001-003] chassis power status")
   except:
      print("test_pipmi exception!")
      print_fail()
      return
   if code == 0:
      print_pass()
   else:
      print_fail()
   print("--- pipmi out ---")
   print(out)
   if err != "":
      print("--- pipmi err ---")
      print(err)
   if code != 0:
      print("--- pipmi code ---")
      print(code)


########################################################################
def test_pping():
   try:
      (out,err,code) = misc.run_cmd("pping wh[001-003]")
   except:
      print("test_pping exception!")
      print_fail()
      return
   if code == 0:
      print_pass()
   else:
      print_fail()
   print("--- pping out ---")
   print(out)
   if err != "":
      print("--- pping err ---")
      print(err)
   if code != 0:
      print("--- pping code ---")
      print(code)


########################################################################
def test_ppower():
   try:
      (out,err,code) = misc.run_cmd("ppower wh[001-003] status")
   except:
      print("test_ppower exception!")
      print_fail()
      return
   if code == 0:
      print_pass()
   else:
      print_fail()
   print("--- ppower out ---")
   print(out)
   if err != "":
      print("--- ppower err ---")
      print(err)
   if code != 0:
      print("--- ppower code ---")
      print(code)


########################################################################
if __name__ == "__main__":
   print(" ")
   test_pcmd()
   print(" ")
   test_pipmi()
   print(" ")
   test_pping()
   print(" ")
   test_ppower()
   print(" ")

