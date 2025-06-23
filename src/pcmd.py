import run
import args
import sys
import util


################################################################################
def pcmd(node, args):

    cmd = args["extra"]
    pcmd_command = f"ssh {node} '{cmd}'"
    if util.is_testing():
        util.print(pcmd_command)
    else:
        out = run.run_cmd(pcmd_command, args["timeout"])
        run.print_output(node, out, args)


################################################################################
def main(argv):

    desc = "Usage: pcmd [OPTIONS] NODELIST COMMAND\n" + \
        "Run a command in parallel across several nodes using ssh"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    args1 = args.parse(argv, desc, desc2)
    run.run_in_parallel(args1["nodelist"], pcmd, (args1,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)

