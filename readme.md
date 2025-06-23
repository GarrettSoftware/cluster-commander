# cluster-commander

The purpose of this software is to control several servers with a single command.
There are 4 main tools:
* pcmd - runs a single command across multiple machines
* pping - runs a single ping across multiple machines
* pipmi - runs an IPMI command across multiple machines
* ppower - runs an IPMI power command across multiple machines.
The tools run in parallel across all servers, so the time taken is about the time required for the action/command on one server.

The following are quick examples to show the power of these tools.
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

## pcmd (Parallel Command)
```
pcmd [OPTIONS] NODELIST COMMAND
```

## pping (Parallel Ping)
```
pping [OPTIONS] NODELIST
```

## pipmi (Parallel IPMI)
```
pipmi [OPTIONS] NODELIST COMMAND
```

## ppower (Parallel Power)
```
ppower [OPTIONS] NODELIST COMMAND
```

## OPTIONS
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

## NODELIST
```
    Comma separated list of nodes.  Nodes can use ranges as well.
    Examples:
      node1,node2,node3,node5,node6,node7
      node[1-3],node[5-7]
      node[1-3,5-7]
      node[01-10]
```

## Installation and Configuration
Just copy the code to a folder of your choice to install.

All configuration is done in the `etc` folder.
Copy each `.example` file to the same name without the `.example` suffix.
Then fill out each configuration file as indicated.

* `env.sh` - Sets the python3 interpreter you want to use.  Python must be at least version 7.
* `alias.txt` - This file holds all alias info.  For instance if you have four servers named `hn[001-004]`, you can create an alias name `hn` for all these nodes.
* `ipmi.txt` - This holds data related to using the IPMI tools.  You may have server `hn001` and the name `hn001-ipmi` associated to the IPMI IP address.  You also need to add login name, password, and cipher suite index.
