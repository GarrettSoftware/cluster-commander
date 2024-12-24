import parse

class Ipmi_Data:

   #####################################################################
   def __init__(self, filename):
      with open(filename, "r") as f:
         lines = f.readlines()

      self.password_list = []
      for line in lines:
         line = line.strip()
         tokens = line.split()
         if len(tokens) == 5:
            node_list1 = parse.parse_node_list(tokens[0])
            node_list2 = parse.parse_node_list(tokens[1])
            for i in range(0, len(node_list1)):
               self.password_list.append(
                  (node_list1[i], node_list2[i], tokens[2], tokens[3], tokens[4]))


   #####################################################################
   def get_command(self, node1):
      for entry in self.password_list:
         if entry[0] == node1:
            node = entry[1]
            user = entry[2]
            password = entry[3]
            cipher = entry[4]
            return f"ipmitool -C {cipher} -I lanplus -H {node} -U {user} -P {password}"
      return ""

