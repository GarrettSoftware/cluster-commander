import sys
import run
import args
import util
import getpass


################################################################################
def psudo(node, arglist, sudo_password):

    cmd = arglist["extra"]
    psudo_command = f"ssh -o LogLevel=ERROR {node} 'sudo -S {cmd}'"
    if util.is_testing():
        util.print(psudo_command)
    else:
        out = run.run_cmd(psudo_command, arglist["timeout"], sudo_password)
        run.print_output(node, out, arglist)


################################################################################
def main(argv):

    desc = "Usage: psudo [OPTIONS] NODELIST [-EXNODELIST] COMMAND\n" + \
        "Run a command in parallel across several nodes using ssh"
    desc2 = "COMMAND:\n" + \
        "  The command to run across each node"

    util.catch_ctrl_c()
    arglist = args.parse(argv, desc, desc2)
    sudo_password = getpass.getpass("Enter sudo password: ")
    run.run_in_parallel(
        arglist["nodelist"], arglist["exnodelist"], psudo, 
        (arglist, sudo_password,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)
