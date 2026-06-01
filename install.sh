#!/bin/bash

SCRIPT_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
echo "Enter an install path: "
read INSTALL_PATH

if [ -e $INSTALL_PATH ]; then
    echo "Install path already exists: $INSTALL_PATH"
    echo "Exiting without install"
    exit 1
fi

echo "Confirm install to: $INSTALL_PATH (y/n)"
read CONFIRM

if [[ $CONFIRM != "y" && $CONFIRM != "Y" ]]; then
    echo "Aborting Install"
    exit 1
fi

echo "Installing ..."
mkdir -p $INSTALL_PATH
mkdir $INSTALL_PATH/bin $INSTALL_PATH/etc $INSTALL_PATH/src
cp $SCRIPT_DIR/bin/* $INSTALL_PATH/bin
cp $SCRIPT_DIR/etc/*.example $INSTALL_PATH/etc
cp $SCRIPT_DIR/src/* $INSTALL_PATH/src
cp $SCRIPT_DIR/*.{txt,md} $INSTALL_PATH

echo "Remember to edit the files in $INSTALL_PATH/etc"
echo "Installation done"
