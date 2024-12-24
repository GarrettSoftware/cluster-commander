# node_list = node_range(,node_range)*
# node_range = name OR name[num_list](name_char)*
# num_list = num_range(,num_range)*
# num_range = num OR num-num
# num = (0-9)+
# name = (a-z or A-Z)(name_char)*
# name_char = (a-z OR A-Z OR 0-9 OR '-' OR '_')

import alias


########################################################################
def ensure_name_char(s):
   if len(s) != 1:
      raise Exception("ensure_name_char")

   if s in "abcdefghijklmnopqrstuvwxyz":
      return None
   if s in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
      return None
   if s in "0123456789":
      return None
   if s in "-_":
      return None

   raise Exception("ensure_name_char")


########################################################################
def ensure_name(s):
   if len(s) == 0:
      raise Exception("ensure_name")
   if not s[0].isalpha():
      raise Exception("ensure_name")
   for i in range(1,len(s)):
      ensure_name_char(s[i])


########################################################################
def ensure_num(s):
   if len(s) == 0:
      raise Exception("ensure_num")
   if not s.isdigit():
      raise Exception("ensure_num")
   

########################################################################
def parse_num_range(s):

   split = s.split("-")

   if len(split) == 1:
      ensure_num(split[0])
      return [split[0]]

   elif len(split) == 2:
      s0 = split[0]
      s1 = split[1]

      ensure_num(s0)
      ensure_num(s1)
      
      i0 = int(split[0])
      i1 = int(split[1])
      
      if i0 >= i1:
         raise Exception("parse_num_range")

      # Format to ensure 001-003 keeps leading zeros
      # Ex {:03d}
      format_string = "{:0" + str(len(s0)) + "d}"
      num_range = []
      for num in range(i0, i1+1):
         num_range.append(format_string.format(num))
      return num_range

   else:
      raise Exception("parse_num_range")


########################################################################
def parse_num_list(s):
   num_list = []
   for num_range in s.split(","):
      num_list.extend(parse_num_range(num_range))
   return num_list


########################################################################
def parse_node_range(s):

   # No brackets
   if s.count("[") == 0 and s.count("]") == 0:
      ensure_name(s)
      return [s]

   # Brackets
   elif s.count("[") == 1 and s.count("]") == 1:
      b1 = s.find("[")
      b2 = s.find("]")

      if b1 == 0 or b1 >= b2:
         raise Exception("parse_node_range")

      node_range = []
      num_list = parse_num_list(s[b1+1:b2])
      prepend = s[0:b1]
      append = s[b2+1:]
      ensure_name(prepend)
      for c in append:
         ensure_name_char(c)

      for num in num_list:
         node_range.append(prepend + num + append)
      return node_range

   # Wrong number of brackets
   else:
      raise Exception("parse_node_range")


########################################################################
def parse_node_list(s):

   # Replace node_range delimiter with |
   # This is done because we can have a comma delimiter for 2 reasons
   # Ex: node[1,3],headnode 
   # Comma delimits both "1,3" and node[1,3] from headnode
   # In this example we change 2nd comma to |
   # Ex: node[1,3],headnode -> node[1,3]|headnode
   # This makes each delimiter unique in its usage
   no_bracket = True
   s1 = ""
   for i in range(0,len(s)):
      if s[i] == "," and no_bracket:
         s1 += "|"
      else:
         s1 += s[i]
      if s[i] == "[":
         no_bracket = False
      elif s[i] == "]":
         no_bracket = True;

   node_list = []
   for node_range in s1.split("|"):
      node_range1 = alias.unalias(node_range)
      node_list.extend(parse_node_range(node_range1))
   return node_list

