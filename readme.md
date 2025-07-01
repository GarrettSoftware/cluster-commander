# cluster-commander

The purpose of this software is to control several servers with a single command.
There are 4 tools:
* pcmd - runs a command across multiple machines
* pping - runs a single ping across multiple machines
* pipmi - runs an IPMI command across multiple machines
* ppower - runs an IPMI power command across multiple machines.
The tools run in parallel across all servers, so the time taken is about the time required for the action/command on one server.

The following are quick examples to show the use of these tools.
Assume we have four servers with hostnames hn001, hn002, hn003, and hn004.
Notice the commands are done in parallel, so the order of output from the servers is random.
However, the output for each server is never split.
```
$ pcmd hn[001-004] hostname
[hn001]: hn001.hpc.bell
[hn003]: hn003.hpc.bell
[hn002]: hn002.hpc.bell
[hn004]: hn004.hpc.bell
```
```
$ ./pping hn[001-004]
[hn001]: ping
[hn004]: ping
[hn002]: ping
[hn003]: ping
```
```
$ ./pipmi hn[001-004] sel list
[hn002]: 1 | 06/16/2025 | 13:31:32 | Event Logging Disabled #0xe1 | Log area reset/cleared | Asserted
[hn003]: 1 | 06/16/2025 | 13:31:33 | Event Logging Disabled #0xe1 | Log area reset/cleared | Asserted
[hn001]: 1 | 06/16/2025 | 13:31:27 | Event Logging Disabled #0xe1 | Log area reset/cleared | Asserted
[hn004]: 1 | 06/16/2025 | 13:31:32 | Event Logging Disabled #0xe1 | Log area reset/cleared | Asserted
```
```
$ ./ppower hn[001-004] status
[hn001]: Chassis Power is on
[hn002]: Chassis Power is on
[hn004]: Chassis Power is on
[hn003]: Chassis Power is on
```

## General Use
The parallel tools have the following syntax.

```
pcmd [OPTIONS] NODELIST COMMAND
pping [OPTIONS] NODELIST
pipmi [OPTIONS] NODELIST COMMAND
ppower [OPTIONS] NODELIST COMMAND
```

The meaning for `OPTIONS` and `NODELIST` is the same for each parallel tool.
The meaning of `COMMAND` is different for each parallel tool.
More information on `OPTIONS`, `NODELIST`, and `COMMAND` is given in the sections below.

### OPTIONS
```
    -h,   --help              Print this help message
    -v,   --version           Print version
    -s,   --space             Add space between each hosts' output
    -e,   --error             Print standard error
    -c,   --code              Print return code
    -d,   --debug             Print command run by this program
    --nc, --no-color          Do not print in color
    -t,   --timeout=TIMEOUT   Set timeout in seconds (default: None)
```

### NODELIST
```
    Comma separated list of nodes, node ranges, and aliases.
    An alias allows you to aggregate nodes into a single name
    such as nodes meaning node[01-10].
    Aliases are specified in the etc/alias.txt file.

    Examples:
      node1,node2,node3,node5,node6,node7
      node[1-3],node[5-7]
      node[1-3,5-7]
      node[01-10]
      nodes
```

### COMMAND
* For `pcmd`, `COMMAND` is any Linux command you would use if you typed `ssh HOST COMMAND`.
* For `pipmi`, `COMMAND` is an IPMI command.
* For `ppower`, `COMMAND` is one of the following:
  * `status`: get power status
  * `on`:     turn on
  * `off`:    turn off
  * `cycle`:  turn off, then on
  * `reset`:  turn off, then on; less of an off state than cycle
  * `soft`:   start OS shutdown


## Installation and Configuration
Copy the code to a folder of your choice to install.

Add the `bin` folder to the PATH for easy access to the parallel tools.
All configuration is done in the `etc` folder.
Copy each `.example` file to the same name without the `.example` suffix.
Then fill out each configuration file as indicated.

* `env.sh` - Sets the python3 interpreter you want to use.  Python must be at least version 7.
* `alias.txt` - This file holds all alias info.
* `ipmi.txt` - This holds data related to using the IPMI tools: `pipmi` and `ppower`.

### Note on Cipher Suite
The `ipmi.txt` file requires you set a cipher suite index for commands.
To find available cipher suites, use the command `ipmitool lan print`.
You will get output similar to the one below.

```
RMCP+ Cipher Suites     : 1,2,3,6,7,8,11,12,15,16,17
Cipher Suite Priv Max   : XXaXXXXXXXaXXXX
                        :     X=Cipher Suite Unused
                        :     c=CALLBACK
                        :     u=USER
                        :     o=OPERATOR
                        :     a=ADMIN
                        :     O=OEM
```

In this case there is an `X` or an `a` for each of the RMCP+ Cipher Suites shown.
To decode this:
* The first two `X`'s mean cipher suites 1 and 2 are unused.
* The 3rd character is an `a` meaning we can use cipher suite 3 for admin work.
* The next 7 `X`s mean cipher suites 6,7,8,11,12,15,16 are unused.
* The next `a` means we can use cipher suite 17 for admin work.


