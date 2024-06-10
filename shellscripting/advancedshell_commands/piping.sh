#!/bin/bash

# Author: Declan Munene
# Date: 10th June, 2024
# title: learnning piping in linux

# Piping, used to move data between commands
# Command 1 -----> Command 2

cat listOffruits.txt | sort # the output of cat which displays the contents of list is given as an argument to the sort command which sorts in alphabetical order

cat listOffruits.txt | grep Peach # looks for the word Peach 

cat listOffruits.txt | head -8

cat listOffruits.txt | head -8 | tail -4
