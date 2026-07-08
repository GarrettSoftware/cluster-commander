# node_list = node_range(,node_range)*
# node_range = name OR name[num_list](name_char)*
# num_list = num_range(,num_range)*
# num_range = num OR num-num
# num = (0-9)+
# name = (a-z or A-Z)(name_char)*
# name_char = (a-z OR A-Z OR 0-9 OR '-' OR '_')

import alias


########################################################################
def ensure_name_char(char):
    if len(char) != 1:
        raise Exception("ensure_name_char")

    if char in "abcdefghijklmnopqrstuvwxyz":
        return None
    if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return None
    if char in "0123456789":
        return None
    if char in "-_":
        return None

    raise Exception("ensure_name_char")


########################################################################
def ensure_name(string):
    if len(string) == 0:
        raise Exception("ensure_name")
    if not string[0].isalpha():
        raise Exception("ensure_name")
    for i in range(1, len(string)):
        ensure_name_char(string[i])


########################################################################
def ensure_num(string):
    if len(string) == 0:
        raise Exception("ensure_num")
    if not string.isdigit():
        raise Exception("ensure_num")


########################################################################
def parse_num_range(string):

    split = string.split("-")

    if len(split) == 1:
        ensure_num(split[0])
        return [split[0]]

    if len(split) == 2:
        string0 = split[0]
        string1 = split[1]

        ensure_num(string0)
        ensure_num(string1)

        idx0 = int(split[0])
        idx1 = int(split[1])

        if idx0 >= idx1:
            raise Exception("parse_num_range")

        # Format to ensure 001-003 keeps leading zeros
        # Ex {:03d}
        format_string = "{:0" + str(len(string0)) + "d}"
        num_range = []
        for num in range(idx0, idx1+1):
            num_range.append(format_string.format(num))
        return num_range

    raise Exception("parse_num_range")


########################################################################
def parse_num_list(string):
    num_list = []
    for num_range in string.split(","):
        num_list.extend(parse_num_range(num_range))
    return num_list


########################################################################
def parse_node_range(string):

    # No brackets
    if string.count("[") == 0 and string.count("]") == 0:
        ensure_name(string)
        return [string]

    # Brackets
    if string.count("[") == 1 and string.count("]") == 1:
        br1 = string.find("[")
        br2 = string.find("]")

        if br1 == 0 or br1 >= br2:
            raise Exception("parse_node_range")

        node_range = []
        num_list = parse_num_list(string[br1+1:br2])
        prepend = string[0:br1]
        append = string[br2+1:]
        ensure_name(prepend)
        for char in append:
            ensure_name_char(char)

        for num in num_list:
            node_range.append(prepend + num + append)
        return node_range

    # Wrong number of brackets
    raise Exception("parse_node_range")


########################################################################
# Replace node_range delimiter with |
# This is done because we can have a comma delimiter for 2 reasons
# Ex: node[1,3],headnode
# Comma delimits both "1,3" and node[1,3] from headnode
# In this example we change 2nd comma to |
# Ex: node[1,3],headnode -> node[1,3]|headnode
# This makes each delimiter unique in its usage
########################################################################
def comma_to_bar_delimiter(string):
    no_bracket = True
    string1 = ""
    for char in string:
        if char == "," and no_bracket:
            string1 += "|"
        else:
            string1 += char
        if char == "[":
            no_bracket = False
        elif char == "]":
            no_bracket = True
    return string1


########################################################################
# Read the comment for comma_to_bar_delimiter.
########################################################################
def parse_node_list(node_string):

    node_string = comma_to_bar_delimiter(node_string)
    node_string_unaliased = ""
    for token in node_string.split("|"):
        token_unaliased = alias.unalias(token)
        node_string_unaliased += "|" + comma_to_bar_delimiter(token_unaliased)

    node_string_unaliased = node_string_unaliased[1:]

    node_list = []
    for token in node_string_unaliased.split("|"):
        node_list.extend(parse_node_range(token))
    return node_list
