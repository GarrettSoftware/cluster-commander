import sys
import threading
import subprocess
import parse
import argparse
import misc


########################################################################
def pping(node, args):

   out = misc.run_cmd(f"ping -c 1 {node}", args.timeout)
   if '1 received' in out[0]:
      out1 = ('ping', out[1], out[2], out[3])
   else:
      out1 = ('no ping', out[1], out[2], out[3])
   misc.print_output(node, out1, args)


########################################################################
if __name__ == "__main__":

   parser = argparse.ArgumentParser(
      prog="pping",
      description="Ping multiple nodes in parallel")

   misc.add_common_parser_options(parser)
   args = misc.parse_args(parser)

   misc.run_in_parallel(args.node_list, pping, (args,))
