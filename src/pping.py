import sys
import run
import args
import util


################################################################################
def pping(node, args):

    pping_command = f"ping -c 1 {node}"
    if util.is_testing():
        util.print(pping_command)
    else:
        out = run.run_cmd(pping_command, args["timeout"])
        if '1 received' in out[0]:
            out1 = ('ping', out[1], out[2], out[3])
        else:
            out1 = ('no ping', out[1], out[2], out[3])
        run.print_output(node, out1, args)


################################################################################
def main(argv):

    desc = "Usage: pping [OPTIONS] NODELIST\n" + \
        "Run ping in parallel across several nodes"

    args1 = args.parse(argv, desc)
    run.run_in_parallel(args1["nodelist"], pping, (args1,))


################################################################################
if __name__ == "__main__":
    main(sys.argv)

