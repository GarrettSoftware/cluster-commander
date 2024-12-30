import os
import socket
import sys
import subprocess
import inspect
import args
import my


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
def test_ensure_name_char():

   try:
      parse.ensure_name_char('a')
      print_pass()
   except:
      print_fail()

   try:
      parse.ensure_name_char('A')
      print_pass()
   except:
      print_fail()
   
   try:
      parse.ensure_name_char('0')
      print_pass()
   except:
      print_fail()
   
   try:
      parse.ensure_name_char('-')
      print_pass()
   except:
      print_fail()
   
   try:
      parse.ensure_name_char('_')
      print_pass()
   except:
      print_fail()
   
   try:
      parse.ensure_name_char('.')
      print_fail()
   except:
      print_pass()
   
   try:
      parse.ensure_name_char('+')
      print_fail()
   except:
      print_pass()


########################################################################
def test_ensure_name():

   try:
      parse.ensure_name('n0aA-_')
      print_pass()
   except:
      print_fail()

   try:
      parse.ensure_name('')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_name('0')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_name('n+')
      print_fail()
   except:
      print_pass()


########################################################################
def test_ensure_num():

   try:
      parse.ensure_num('0')
      print_pass()
   except:
      print_fail()

   try:
      parse.ensure_num('001')
      print_pass()
   except:
      print_fail()

   try:
      parse.ensure_num('')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_num('1a')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_num('+1')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_num('-1')
      print_fail()
   except:
      print_pass()

   try:
      parse.ensure_num('0.1')
      print_fail()
   except:
      print_pass()


########################################################################
def test_parse_num_range():

   if parse.parse_num_range('001') == ['001']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_range('9-10') == ['9','10']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_range('0-3') == ['0','1','2','3']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_range('00-03') == ['00','01','02','03']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_range('001-004') == ['001','002','003','004']:
      print_pass()
   else:
      print_fail()

   try:
      parse.parse_num_range('asdf')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('0.1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('+1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('-1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('2-1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('a-b')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('1-1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_num_range('1-2-3')
      print_fail()
   except:
      print_pass()


########################################################################
def test_parse_num_list():

   if parse.parse_num_list('001') == ['001']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_list('001,003') == ['001','003']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_list('001-003,7') == ['001','002','003','7']:
      print_pass()
   else:
      print_fail()

   if parse.parse_num_list('001-003,7-8') == ['001','002','003','7','8']:
      print_pass()
   else:
      print_fail()


########################################################################
def test_print_help():

    my.set_testing()

    help2a = ""
    help2a += "Description 1\n"
    help2a += "\n"

    help2b = ""
    help2b += "OPTIONS:\n"
    help2b += "  -h,  --help               Print this help message\n"
    help2b += "  -v,  --version            Print version\n"
    help2b += "  -s,  --space              Add space between hosts\n"
    help2b += "  -e,  --error              Print standard error\n"
    help2b += "  -c,  --code               Print return code\n"
    help2b += "  -d,  --debug              Print command run by this program\n"
    help2b += "  --nc, --no-color          Do not print in color\n"
    help2b += "  -t,   --timeout=TIMEOUT   Set timeout in seconds for commands (default: 10)\n"
    help2b += "\n"
    help2b += "NODELIST:\n"
    help2b += "  Comma separated list of nodes.  Nodes can use ranges as well.\n"
    help2b += "  Examples:\n"
    help2b += "    node1,node2,node3,node5,node6,node7\n"
    help2b += "    node[1-3],node[5-7]\n"
    help2b += "    node[1-3,5-7]\n"
    help2b += "    node[01-10]\n"

    help2c = ""
    help2c += "\n"
    help2c += "Description 2\n"

    args.print_help("Description 1", "")
    help1 = my.get_and_reset_print_buffer()
    if help1 == help2a + help2b:
        print_pass()
    else:
        print_fail()

    args.print_help("Description 1", "Description 2")
    help1 = my.get_and_reset_print_buffer()
    if help1 == help2a + help2b + help2c:
        print_pass()
    else:
        print_fail()


########################################################################
def test_parse_timeout():

    try:
        args.parse_timeout("")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    try:
        args.parse_timeout("a")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    try:
        args.parse_timeout("01234a")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    try:
        args.parse_timeout("1000000001")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    try:
        args.parse_timeout("0")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    try:
        args.parse_timeout("00000")
        print_fail()
    except SystemExit as e:
        if e.code == 1:
            print_pass()
        else:
            print_fail()

    if args.parse_timeout("1") == 1:
        print_pass()
    else:
        print_fail()

    if args.parse_timeout("01") == 1:
        print_pass()
    else:
        print_fail()

    if args.parse_timeout("1000") == 1000:
        print_pass()
    else:
        print_fail()

    if args.parse_timeout("1000000000") == 1000000000:
        print_pass()
    else:
        print_fail()


########################################################################
if __name__ == "__main__":
    #test_ensure_name_char()
    #test_ensure_name()
    #test_ensure_num()
    #test_parse_num_range()
    #test_parse_num_list()
    #test_parse_node_range()
    test_print_help()
    test_parse_timeout()

