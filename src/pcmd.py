import run
import args
import sys


########################################################################
def pcmd(node, args):

    cmd = args["extra"]
    out = run.run_cmd(f"ssh {node} '{cmd}'", args["timeout"])
    run.print_output(node, out, args)


########################################################################
if __name__ == "__main__":

    desc = "Usage: pcmd [OPTIONS] NODELIST COMMAND\n" + \
        "Run a command in parallel across several nodes using ssh"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    args = args.parse(sys.argv, desc, desc2)
    run.run_in_parallel(args["nodelist"], pcmd, (args,))

