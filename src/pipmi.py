import args
import run
import ipmi
import sys
import util


################################################################################
def pipmi(node, args):

    ipmi_command = ipmi.get_command(node)
    ipmi_command += " " + args["extra"]
    if util.is_testing():
        util.print(ipmi_command)
    else:
        out = run.run_cmd(ipmi_command, args["timeout"])
        run.print_output(node, out, args)


################################################################################
def main(argv):

    desc = "Usage: pipmi [OPTIONS] NODELIST COMMAND\n" + \
        "Run an IPMI command in parallel across several nodes"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    args1 = args.parse(argv, desc, desc2)
    ipmi.read_etc(util.get_root_dir() + "/etc/ipmi.txt")
    run.run_in_parallel(args1["nodelist"], pipmi, (args1,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)

