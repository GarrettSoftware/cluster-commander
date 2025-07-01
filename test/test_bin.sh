#!/bin/bash

# This tests all the binaries in the bin directory
# These are full system tests

/usr/bin/python3.12 -B $(dirname $(realpath $0) )/src/test_bin.py

