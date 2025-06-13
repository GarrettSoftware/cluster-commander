#!/bin/bash

# Get program path and source include file
ROOTDIR=$(dirname $(dirname $(realpath $0) ) )
source $ROOTDIR/etc/env.sh

# Check num parameters
if [[ $# < 1 ]]; then
    echo "Error: run.sh no command given"
    exit 1
fi

# Get command name and pop it off parameter list
CMD=$1
shift

# Do appropriate command
if [[ $CMD == "pcmd" ]]; then
    $PYTHON3 -B $ROOTDIR/src/$CMD.py "$@"
elif [[ $CMD == "pcopy" ]]; then
    $PYTHON3 -B $ROOTDIR/src/$CMD.py "$@"
elif [[ $CMD == "pipmi" ]]; then
    $PYTHON3 -B $ROOTDIR/src/$CMD.py "$@"
elif [[ $CMD == "pping" ]]; then
    $PYTHON3 -B $ROOTDIR/src/$CMD.py "$@"
elif [[ $CMD == "ppower" ]]; then
    $PYTHON3 -B $ROOTDIR/src/$CMD.py "$@"
else
    echo "Error: run.sh did not recognize command"
    exit 1
fi

