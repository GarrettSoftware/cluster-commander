import threading
import parse
import argparse
import misc
import ipmi
import os


########################################################################
def pipmi(node, args, ipmi_data):

   ipmi_command = ipmi_data.get_command(node)
   ipmi_command += " " + args.command
   out = misc.run_cmd(ipmi_command, args.timeout)
   misc.print_output(node, out, args)


########################################################################
if __name__ == "__main__":

   parser = argparse.ArgumentParser(
      prog="pipmi",
      description="Issue IPMI commands in parallel across multiple nodes")

   misc.add_common_parser_options(parser)
   parser.add_argument("command", help="IPMI command to run on nodes")
   args = misc.parse_args(parser)

   path = os.environ["HPC_TOOLS_PATH"]
   ipmi_data = ipmi.Ipmi_Data(path + "/etc/ipmi.txt")

   misc.run_in_parallel(args.node_list, pipmi, (args,ipmi_data,))
