import argparse
import misc
import ipmi
import os


########################################################################
def ppower(node, args, ipmi_data):

   ipmi_command = ipmi_data.get_command(node)

   if args.command == "status":
      ipmi_command += " power status"
   elif args.command == "on":
      ipmi_command += " power on"
   elif args.command == "off":
      ipmi_command += " power off"
   elif args.command == "cycle":
      ipmi_command += " power cycle"
   elif args.command == "reset":
      ipmi_command += " power reset"
   elif args.command == "soft":
      ipmi_command += " power soft"
   else:
      print(args.command + ": command not supported")
      return

   out = misc.run_cmd(ipmi_command, args.timeout)
   misc.print_output(node, out, args)


########################################################################
if __name__ == "__main__":

   description = \
         "Issue IPMI power commands in parallel across multiple nodes.\n" + \
         "Each command calls the equivalent IPMI power command.\n" + \
         "  status: get power status\n" + \
         "  on:     turn on\n" + \
         "  off:    turn off\n" + \
         "  cycle:  turn off, then on\n" + \
         "  reset:  turn off, then on; less of an off state than cycle\n" + \
         "  soft:   start OS shutdown"
      
   parser = argparse.ArgumentParser(
      prog="ppower", formatter_class=argparse.RawTextHelpFormatter,
      description=description)

   misc.add_common_parser_options(parser)
   parser.add_argument("command", 
      help="IPMI power command")
   args = misc.parse_args(parser)

   path = os.environ["HPC_TOOLS_PATH"]
   ipmi_data = ipmi.Ipmi_Data(path + "/etc/ipmi.txt")

   misc.run_in_parallel(args.node_list, ppower, (args,ipmi_data,))
