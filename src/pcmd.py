import argparse
import misc


########################################################################
def pcmd(node, args):

   out = misc.run_cmd(f"ssh {node} '{args.command}'", args.timeout)
   misc.print_output(node, out, args)


########################################################################
if __name__ == "__main__":

   parser = argparse.ArgumentParser(
      prog="pcmd",
      description="Run a command in parallel across several nodes using ssh")

   misc.add_common_parser_options(parser)
   parser.add_argument("command", help="Command to run on nodes")
   args = misc.parse_args(parser)

   misc.run_in_parallel(args.node_list, pcmd, (args,))
