#!/bin/bash

run_test() {
    echo ----- $1 -----
    /usr/bin/python3.12 -B $(dirname $(realpath $0) )/src/$1
    echo " "
}

if [[ $# == 0 ]]; then
    run_test test_alias.py
    run_test test_args.py
    run_test test_parse.py
    run_test test_pipmi.py
    exit 0
elif [[ $1 == "alias" ]]; then
    run_test test_alias.py
elif [[ $1 == "args" ]]; then
    run_test test_args.py
elif [[ $1 == "parse" ]]; then
    run_test test_parse.py
elif [[ $1 == "pipmi" ]]; then
    run_test test_pipmi.py
fi
