import parse
import util


PASSWORD_LIST = []

################################################################################
def read_etc(filename):

    if util.is_testing() and PASSWORD_LIST != []:
        return

    with open(filename, "r") as fil:
        lines = fil.readlines()

    line_num = 0
    for line in lines:
        line = line.strip()
        line_num = line_num + 1

        # Comment
        if line[0:1] == "#":
            continue
        # Blank line
        if line == "":
            continue

        tokens = line.split()
        if len(tokens) == 5:
            node_list1 = parse.parse_node_list(tokens[0])
            node_list2 = parse.parse_node_list(tokens[1])
            for node1, node2 in zip(node_list1, node_list2):
                PASSWORD_LIST.append(
                    (node1, node2, tokens[2], tokens[3], tokens[4]))
        else:
            util.print(f"Error in {filename}")
            util.print(f"Wrong number of tokens on line: {line_num}")


################################################################################
def get_command(node1):
    for entry in PASSWORD_LIST:
        if entry[0] == node1:
            node = entry[1]
            user = entry[2]
            password = entry[3]
            cipher = entry[4]
            return f"ipmitool -C {cipher} -I lanplus -H {node} -U {user} -P {password}"
    return ""
