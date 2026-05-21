import sys
import run
import args
import util


################################################################################
def pcmd(node, arglist):

    cmd = arglist["extra"]
    pcmd_command = f"ssh -o LogLevel=ERROR {node} '{cmd}'"
    if util.is_testing():
        util.print(pcmd_command)
    else:
        out = run.run_cmd(pcmd_command, arglist["timeout"])
        run.print_output(node, out, arglist)


################################################################################
def main(argv):

    desc = "Usage: pcmd [OPTIONS] NODELIST [-EXNODELIST] COMMAND\n" + \
        "Run a command in parallel across several nodes using ssh"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    util.catch_ctrl_c()
    arglist = args.parse(argv, desc, desc2)
    run.run_in_parallel(
        arglist["nodelist"], arglist["exnodelist"], pcmd, (arglist,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)
