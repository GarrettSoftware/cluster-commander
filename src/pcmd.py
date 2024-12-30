import misc
import args
import sys


########################################################################
def pcmd(node, args):

    cmd = args["extra"]
    out = misc.run_cmd(f"ssh {node} '{cmd}'", args["timeout"])
    misc.print_output(node, out, args)


########################################################################
if __name__ == "__main__":

    prog="pcmd"
    desc = "Usage: pcmd [OPTIONS] NODELIST COMMAND\n" + \
        "Run a command in parallel across several nodes using ssh"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    args = args.parse(sys.argv, prog, desc, desc2)
    misc.run_in_parallel(args["nodelist"], pcmd, (args,))

