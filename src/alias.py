########################################################################
# Parses a file of aliases and returns the alias if it is in the file.
# If the alias is not in the file, the original name is returned.
#
# Each line has one of the 3 following formats
#   (whitespace)* (comment)?
#   (whitespace)* name1 (whitespace)+ name2 (whitespace)* (comment)?
#   name1 = (alpha)(alpha OR num OR '-' OR '_')*
#   name2 = (alpha)(alpha OR num OR '-' OR '_' OR '[' OR ']')*
#
# If a line does not conform to a recognized format, it is skipped
########################################################################
import util


########################################################################
def unalias(name):

    # Read alias file
    path = util.get_root_dir()
    with open(path + "/etc/alias.txt", "r") as fil:
        lines = fil.readlines()

    # Try to find the alias
    for line in lines:
        # Get rid of comments
        comment_pos = line.find('#')
        if line.find('#') >= 0:
            line = line[:comment_pos]

        # Get rid of whitespace at front and end
        line = line.strip()

        # Split line
        tokens = line.split()

        # Ensure line is correct format
        if len(tokens) != 2:
            continue
        if not ensure_name1(tokens[0]):
            continue
        if not ensure_name2(tokens[1]):
            continue

        # See if we found the correct alias
        if tokens[0] == name:
            return tokens[1]

    # No alias found
    return name


########################################################################
def ensure_name1(string):
    if len(string) == 0:
        return False
    if not string[0].isalpha():
        return False
    for i in range(1, len(string)):
        if not string[i].isalnum() and not string[i] in "-_":
            return False
    return True


########################################################################
def ensure_name2(string):
    if len(string) == 0:
        return False
    if not string[0].isalpha():
        return False
    for i in range(1, len(string)):
        if not string[i].isalnum() and not string[i] in "-_[]":
            return False
    return True
