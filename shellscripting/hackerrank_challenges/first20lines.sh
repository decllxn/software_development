#!/bin/bash

# Author: Declan Munene
# Date: 10th June
# Description: head command to display first 20 lines of an input

read -p "Enter file name: " file

head -20 $file
