import subprocess
import threading
import time
import parse
import util

PRINT_LOCK = threading.Lock()


################################################################################
# Run a command on the terminal and return:
#    stdout, stderr, and the return code
################################################################################
def run_cmd(cmd, timeout):

    try:
        proc = subprocess.run(
            cmd, capture_output=True, shell=True,
            timeout=timeout, check=False)
        out = proc.stdout.decode('utf-8', errors='ignore').strip()
        err = proc.stderr.decode('utf-8', errors='ignore').strip()
        code = proc.returncode
    except subprocess.TimeoutExpired:
        out = f"<timeout: {timeout}s>"
        err = ""
        code = -1

    return (out, err, code, cmd)


################################################################################
# Prints stdout.
# Can optionally print stderr and return code.
# Can optionally print space after everything else.
# Can optionally print in color for node names.
################################################################################
def print_output(node, out, args):

    # Gives time to turn off printing across threads
    time.sleep(0.25)

    if not args["color"]:
        node_string = f"[{node}]"
        err_node_string = f"[STDERR {node}]"
        debug_node_string = f"[DEBUG {node}]"
    else:
        node_string = f"\033[1;32m[{node}]\033[0m"
        err_node_string = f"\033[1;31m[STDERR {node}]\033[0m"
        debug_node_string = f"\033[1;35m[DEBUG {node}]\033[0m"

    stdout = out[0]
    stderr = out[1]
    code = out[2]
    cmd = out[3]

    out1 = ""
    if args["debug"]:
        out1 += f"{debug_node_string}:  CMD: {cmd}  CODE: {code}\n"
    if stderr != "":
        for line in stderr.split("\n"):
            out1 += f"{err_node_string}: {line}\n"
    if stdout == "":
        out1 += f"{node_string}: <no output>\n"
    else:
        for line in stdout.split("\n"):
            out1 += f"{node_string}: {line}\n"
    if not args["space"]:
        out1 = out1.strip()

    with PRINT_LOCK:
        util.print(out1)


################################################################################
def run_in_parallel(node_list_string, ex_node_list_string, function, args):

    node_list = parse.parse_node_list(node_list_string)
    if ex_node_list_string != "":
        ex_node_list = parse.parse_node_list(ex_node_list_string)
        for node in ex_node_list:
            if node in node_list:
                node_list.remove(node)
            else:
                util.print(f"Warning: exclude node [{node}] not in nodelist")

    threadlist = []
    for node in node_list:
        args1 = (node,) + args
        thread = threading.Thread(target=function, args=args1)
        thread.start()
        threadlist.append(thread)

    for thread in threadlist:
        thread.join()
