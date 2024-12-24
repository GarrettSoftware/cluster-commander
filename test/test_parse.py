import os
import socket
import sys
import subprocess
import inspect
import parse


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
def test_parse_node_range():

   if parse.parse_node_range('node1') == ['node1']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_range('node[1-3]') == ['node1','node2','node3']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_range('node[1-3]-ipmi') == ['node1-ipmi','node2-ipmi','node3-ipmi']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_range('node[001-003]') == ['node001','node002','node003']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_range('n[1-3,05-07,9]') == ['n1','n2','n3','n05','n06','n07','n9']:
      print_pass()
   else:
      print_fail()

   try:
      parse.parse_node_range('')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('n+1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('[123]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('n[3-1]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('n[1-3]]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('n[1-3][5-7]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_range('n]1-3[')
      print_fail()
   except:
      print_pass()


########################################################################
def test_parse_node_list():

   if parse.parse_node_list('node1') == ['node1']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_list('node[1-3]') == ['node1','node2','node3']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_list('node[001-003]') == ['node001','node002','node003']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_list('n[1-3,05-07,9]') == ['n1','n2','n3','n05','n06','n07','n9']:
      print_pass()
   else:
      print_fail()

   if parse.parse_node_list('n[1-3,05-07,9],airwolf') == ['n1','n2','n3','n05','n06','n07','n9','airwolf']:
      print_pass()
   else:
      print_fail()

   try:
      parse.parse_node_list('')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_list('1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_list('n+1')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_list('[123]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_list('n[3-1]')
      print_fail()
   except:
      print_pass()

   try:
      parse.parse_node_list('n]1-3[')
      print_fail()
   except:
      print_pass()


########################################################################
if __name__ == "__main__":
   test_ensure_name_char()
   test_ensure_name()
   test_ensure_num()
   test_parse_num_range()
   test_parse_num_list()
   test_parse_node_range()
   test_parse_node_list()

