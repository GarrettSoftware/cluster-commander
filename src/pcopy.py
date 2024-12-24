import argparse
import misc
import sys
import os


########################################################################
def split_copy_args(args):
   tokens = args.split()
   if len(tokens) != 2:
      raise Exception("Wrong number of copy arguments")
   if not os.path.exists(tokens[0]):
      raise Exception("Source does not exist")
   if tokens[1][0] != "/":
      raise Exception("Destination must be an absolute path")
   return (tokens[0], tokens[1])


########################################################################
def pcopy(node, args):

   try:
      (src, dest) = split_copy_args(args.copy_args)
   except Exception as e:
      print(e)
      sys.exit(1)
   out = misc.run_cmd(f"scp -r '{src}' {node}:'\"{dest}\"'", args.timeout)
   if out[2] == 0:
      out1 = ('Copy Succeeded', out[1], out[2], out[3])
   else:
      out1 = ('Copy Failed', out[1], out[2], out[3])
   misc.print_output(node, out1, args)


########################################################################
if __name__ == "__main__":

   parser = argparse.ArgumentParser(
      prog="pcopy",
      description="Copy file to multiple nodes")

   misc.add_common_parser_options(parser)
   parser.add_argument("copy_args", help="copy arguments")
   args = misc.parse_args(parser)

   misc.run_in_parallel(args.node_list, pcopy, (args,))
