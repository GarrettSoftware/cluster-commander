#!/bin/bash

run_test() {
    echo ----- $1 -----
    /usr/bin/python3.12 -B $(dirname $(realpath $0) )/src/$1
    echo " "
}

if [[ $# == 0 ]]; then
    run_test test_alias.py
    run_test test_args.py
    run_test test_ipmi.py
    run_test test_parse.py
    run_test test_pcmd.py
    run_test test_pipmi.py
    run_test test_pping.py
    run_test test_ppower.py
    run_test test_run.py
    run_test test_util.py
    exit 0
elif [[ $1 == "alias" ]]; then
    run_test test_alias.py
elif [[ $1 == "args" ]]; then
    run_test test_args.py
elif [[ $1 == "ipmi" ]]; then
    run_test test_ipmi.py
elif [[ $1 == "parse" ]]; then
    run_test test_parse.py
elif [[ $1 == "pcmd" ]]; then
    run_test test_pcmd.py
elif [[ $1 == "pipmi" ]]; then
    run_test test_pipmi.py
elif [[ $1 == "pping" ]]; then
    run_test test_pping.py
elif [[ $1 == "ppower" ]]; then
    run_test test_ppower.py
elif [[ $1 == "run" ]]; then
    run_test test_run.py
elif [[ $1 == "util" ]]; then
    run_test test_util.py
fi
