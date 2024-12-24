import subprocess
import argparse
import sys
import threading
import os

import parse

print_lock = threading.Lock()


########################################################################
# Run a command on the terminal and return:
#    stdout, stderr, and the return code
########################################################################
def run_cmd(cmd, timeout):

   try:
      proc = subprocess.run(cmd, capture_output=True, shell=True, timeout=timeout)
      out = proc.stdout.decode('utf-8',errors='ignore').strip()
      err = proc.stderr.decode('utf-8',errors='ignore').strip()
      code = proc.returncode
   except:
      out = f"<timeout: {timeout}s>"
      err = f"<timeout: {timeout}s>"
      code = -1

   return (out, err, code, cmd)


########################################################################
# Prints stdout.
# Can optionally print stderr and return code.
# Can optionally print space after everything else.
# Can optionally print in color for node names.
########################################################################
def print_output(node, out, args):

   if args.nc:
      node_string = f"[{node}]"
      err_node_string = f"[STDERR {node}]"
      code_node_string = f"[CODE {node}]"
      debug_node_string = f"[DEBUG {node}]"
   else:
      node_string = f"\033[1;32m[{node}]\033[0m"
      err_node_string = f"\033[1;31m[STDERR {node}]\033[0m"
      code_node_string = f"\033[1;33m[CODE {node}]\033[0m"
      debug_node_string = f"\033[1;35m[DEBUG {node}]\033[0m"

   stdout = out[0]
   stderr = out[1]
   code = out[2]
   cmd = out[3]

   out1 = ""
   for line in stdout.split("\n"):
      out1 += f"{node_string}: {line}\n"
   if args.error:
      for line in stderr.split("\n"):
         out1 += f"{err_node_string}: {line}\n"
   if args.code:
      out1 += f"{code_node_string}: {code}\n"
   if args.debug:
      out1 += f"{debug_node_string}: {cmd}\n"
   if not args.space:
      out1 = out1.strip()

   with print_lock:
      print(out1)


########################################################################
# These are common parse options for all commands
########################################################################
def add_common_parser_options(parser, nodelist=True):

   parser.add_argument(
      "-v", "--version", action='store_true', 
      help="Display version", default=False)
   parser.add_argument(
      "-s", "--space", action='store_true', 
      help="Add space between hosts", default=False)
   parser.add_argument(
      "-e", "--error", action='store_true', 
      help="Print standard error", default=False)
   parser.add_argument(
      "-c", "--code", action='store_true', 
      help="Print return code", default=False)
   parser.add_argument(
      "-d", "--debug", action='store_true', 
      help="Print command", default=False)
   parser.add_argument(
      "--nc", "--no-color", action='store_true', 
      help="Do not print color", default=False)
   parser.add_argument(
      "-t", "--timeout", type=int, 
      help="Print return code", default=10)
   if nodelist:
      parser.add_argument("node_list", help="List of nodes")


########################################################################
# Had to reimplement parser.parse_args.
# Found a bug where:
#    pcmd wh hostname -s 
# would output spaces and not do the -s for short.
# Only want - options before other options
# This changes the sys.argv list into:
#    argv[0-N] = - options
#    argv[N+1] = node_list
#    argv[N+2] = all other arguments (usually commands)
########################################################################
def parse_args(parser):
   argv = []
   state = "dashes"
   cmd = ""
   nodelist = ""
   for arg in sys.argv[1:]:
      if state == "dashes":
         if arg[0] == '-':
            argv.append(arg)
         else:
            state = "command"
            nodelist = arg
      elif state == "command":
         cmd += arg + ' '

   # Check for version
   temp_parser = argparse.ArgumentParser()
   add_common_parser_options(temp_parser, nodelist=False)
   args = temp_parser.parse_args(argv)
   if args.version:
      path = os.environ["HPC_TOOLS_PATH"]
      os.system(f"echo Version $(cat {path}/version.txt)")
      sys.exit(0)

   # Add nodelist
   if nodelist.strip() != "":
      argv.append(nodelist)

   # Add command as one argument even if it contains spaces
   if cmd.strip() != "":
      argv.append(cmd.strip())

   return parser.parse_args(argv)


########################################################################
def run_in_parallel(node_list_string, target, args):

   node_list = parse.parse_node_list(node_list_string)

   threadlist = []
   for node in node_list:
      args1 = (node,) + args
      t = threading.Thread(target=target, args=args1)
      t.start()
      threadlist.append(t)

   for t in threadlist:
      t.join()

