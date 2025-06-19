import os
import socket
import sys
import subprocess
import inspect
import test

sys.path.append("../src")
import parse



########################################################################
def test_ensure_name_char():

   try:
      parse.ensure_name_char('a')
      test.print_pass()
   except:
      test.print_fail()

   try:
      parse.ensure_name_char('A')
      test.print_pass()
   except:
      test.print_fail()
   
   try:
      parse.ensure_name_char('0')
      test.print_pass()
   except:
      test.print_fail()
   
   try:
      parse.ensure_name_char('-')
      test.print_pass()
   except:
      test.print_fail()
   
   try:
      parse.ensure_name_char('_')
      test.print_pass()
   except:
      test.print_fail()
   
   try:
      parse.ensure_name_char('.')
      test.print_fail()
   except:
      test.print_pass()
   
   try:
      parse.ensure_name_char('+')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
def test_ensure_name():

   try:
      parse.ensure_name('n0aA-_')
      test.print_pass()
   except:
      test.print_fail()

   try:
      parse.ensure_name('')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_name('0')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_name('n+')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
def test_ensure_num():

   try:
      parse.ensure_num('0')
      test.print_pass()
   except:
      test.print_fail()

   try:
      parse.ensure_num('001')
      test.print_pass()
   except:
      test.print_fail()

   try:
      parse.ensure_num('')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_num('1a')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_num('+1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_num('-1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.ensure_num('0.1')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
def test_parse_num_range():

   if parse.parse_num_range('001') == ['001']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_range('9-10') == ['9','10']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_range('0-3') == ['0','1','2','3']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_range('00-03') == ['00','01','02','03']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_range('001-004') == ['001','002','003','004']:
      test.print_pass()
   else:
      test.print_fail()

   try:
      parse.parse_num_range('asdf')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('0.1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('+1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('-1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('2-1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('a-b')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('1-1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_num_range('1-2-3')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
def test_parse_num_list():

   if parse.parse_num_list('001') == ['001']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_list('001,003') == ['001','003']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_list('001-003,7') == ['001','002','003','7']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_num_list('001-003,7-8') == ['001','002','003','7','8']:
      test.print_pass()
   else:
      test.print_fail()


########################################################################
def test_parse_node_range():

   if parse.parse_node_range('node1') == ['node1']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_range('node[1-3]') == ['node1','node2','node3']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_range('node[1-3]-ipmi') == ['node1-ipmi','node2-ipmi','node3-ipmi']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_range('node[001-003]') == ['node001','node002','node003']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_range('n[1-3,05-07,9]') == ['n1','n2','n3','n05','n06','n07','n9']:
      test.print_pass()
   else:
      test.print_fail()

   try:
      parse.parse_node_range('')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('n+1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('[123]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('n[3-1]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('n[1-3]]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('n[1-3][5-7]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_range('n]1-3[')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
def test_parse_node_list():

   if parse.parse_node_list('node1') == ['node1']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_list('node[1-3]') == ['node1','node2','node3']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_list('node[001-003]') == ['node001','node002','node003']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_list('n[1-3,05-07,9]') == ['n1','n2','n3','n05','n06','n07','n9']:
      test.print_pass()
   else:
      test.print_fail()

   if parse.parse_node_list('n[1-3,05-07,9],airwolf') == ['n1','n2','n3','n05','n06','n07','n9','airwolf']:
      test.print_pass()
   else:
      test.print_fail()

   try:
      parse.parse_node_list('')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_list('1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_list('n+1')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_list('[123]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_list('n[3-1]')
      test.print_fail()
   except:
      test.print_pass()

   try:
      parse.parse_node_list('n]1-3[')
      test.print_fail()
   except:
      test.print_pass()


########################################################################
if __name__ == "__main__":
   test_ensure_name_char()
   test_ensure_name()
   test_ensure_num()
   test_parse_num_range()
   test_parse_num_list()
   test_parse_node_range()
   test_parse_node_list()

