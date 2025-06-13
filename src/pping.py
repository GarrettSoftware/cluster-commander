import sys
import run
import args


########################################################################
def pping(node, args):

    out = run.run_cmd(f"ping -c 1 {node}", args["timeout"])
    if '1 received' in out[0]:
        out1 = ('ping', out[1], out[2], out[3])
    else:
        out1 = ('no ping', out[1], out[2], out[3])
    run.print_output(node, out1, args)


########################################################################
if __name__ == "__main__":

    desc = "Ping multiple nodes in parallel"

    args = args.parse(sys.argv, desc)
    run.run_in_parallel(args["nodelist"], pping, (args,))
