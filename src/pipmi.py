import sys
import args
import run
import ipmi
import util


################################################################################
def pipmi(node, arglist):

    ipmi_command = ipmi.get_command(node)
    ipmi_command += " " + arglist["extra"]
    if util.is_testing():
        util.print(ipmi_command)
    else:
        out = run.run_cmd(ipmi_command, arglist["timeout"])
        run.print_output(node, out, arglist)


################################################################################
def main(argv):

    desc = "Usage: pipmi [OPTIONS] NODELIST [-EXNODELIST] COMMAND\n" + \
        "Run an IPMI command in parallel across several nodes"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    util.catch_ctrl_c()
    arglist = args.parse(argv, desc, desc2)
    ipmi.read_etc(util.get_root_dir() + "/etc/ipmi.txt")
    run.run_in_parallel(
        arglist["nodelist"], arglist["exnodelist"], pipmi, (arglist,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)
