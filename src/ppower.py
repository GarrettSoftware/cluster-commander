import args
import run
import ipmi
import sys
import util


################################################################################
def ppower(node, args):

    ipmi_command = ipmi.get_command(node)
    args_command = args["extra"]

    if args_command == "status":
        ipmi_command += " power status"
    elif args_command == "on":
        ipmi_command += " power on"
    elif args_command == "off":
        ipmi_command += " power off"
    elif args_command == "cycle":
        ipmi_command += " power cycle"
    elif args_command == "reset":
        ipmi_command += " power reset"
    elif args_command == "soft":
        ipmi_command += " power soft"
    else:
        util.print(args_command + ": command not supported")
        return

    if util.is_testing():
        util.print(ipmi_command)
    else:
        out = run.run_cmd(ipmi_command, args["timeout"])
        run.print_output(node, out, args)


################################################################################
def main(argv):

    desc = "Usage: ppower [OPTIONS] NODELIST COMMAND\n" + \
        "Run an IPMI power command in parallel across several nodes"
    desc2 = "COMMAND can be any of the following:\n" + \
        "  status: get power status\n" + \
        "  on:     turn on\n" + \
        "  off:    turn off\n" + \
        "  cycle:  turn off, then on\n" + \
        "  reset:  turn off, then on; less of an off state than cycle\n" + \
        "  soft:   start OS shutdown"

    args1 = args.parse(argv, desc, desc2)
    ipmi.read_etc(util.get_root_dir() + "/etc/ipmi.txt")
    run.run_in_parallel(args1["nodelist"], ppower, (args1,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)

