import parse
import util


password_list = []

################################################################################
def read_etc(filename):

    if util.is_testing() and password_list != []:
        return

    with open(filename, "r") as f:
        lines = f.readlines()

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
            for i in range(0, len(node_list1)):
                password_list.append(
                    (node_list1[i], node_list2[i], tokens[2], tokens[3], tokens[4]))
        else:
            util.print(f"Error in {filename}")
            util.print(f"Wrong number of tokens on line: {line_num}")


################################################################################
def get_command(node1):
    for entry in password_list:
        if entry[0] == node1:
            node = entry[1]
            user = entry[2]
            password = entry[3]
            cipher = entry[4]
            return f"ipmitool -C {cipher} -I lanplus -H {node} -U {user} -P {password}"
    return ""

