import subprocess
import threading
import parse
import util

print_lock = threading.Lock()


################################################################################
# Run a command on the terminal and return:
#    stdout, stderr, and the return code
################################################################################
def run_cmd(cmd, timeout):

    try:
        proc = subprocess.run(cmd, capture_output=True, shell=True, 
            timeout=timeout)
        out = proc.stdout.decode('utf-8',errors='ignore').strip()
        err = proc.stderr.decode('utf-8',errors='ignore').strip()
        code = proc.returncode
    except:
        out = f"<timeout: {timeout}s>"
        err = f"<timeout: {timeout}s>"
        code = -1

    return (out, err, code, cmd)


################################################################################
# Prints stdout.
# Can optionally print stderr and return code.
# Can optionally print space after everything else.
# Can optionally print in color for node names.
################################################################################
def print_output(node, out, args):

    if not args["color"]:
        node_string = f"[{node}]"
        err_node_string = f"[STDERR {node}]"
        code_node_string = f"[CODE {node}]"
        debug_node_string = f"[DEBUG {node}]"
    else:
        node_string = f"\033[1;32m[{node}]\033[0m"
        err_node_string = f"\033[1;31m[STDERR {node}]\033[0m"
        code_node_string = f"\033[1;33m[CODE {node}]\033[0m"
        debug_node_string = f"\033[1;35m[DEBUG {node}]\033[0m"

    stdout = out[0]
    stderr = out[1]
    code = out[2]
    cmd = out[3]

    out1 = ""
    for line in stdout.split("\n"):
        out1 += f"{node_string}: {line}\n"
    if args["error"]:
        for line in stderr.split("\n"):
            out1 += f"{err_node_string}: {line}\n"
    if args["code"]:
        out1 += f"{code_node_string}: {code}\n"
    if args["debug"]:
        out1 += f"{debug_node_string}: {cmd}\n"
    if not args["space"]:
        out1 = out1.strip()

    with print_lock:
        util.print(out1)


################################################################################
def run_in_parallel(node_list_string, function, args):

    node_list = parse.parse_node_list(node_list_string)

    threadlist = []
    for node in node_list:
        args1 = (node,) + args
        t = threading.Thread(target=function, args=args1)
        t.start()
        threadlist.append(t)

    for t in threadlist:
        t.join()

