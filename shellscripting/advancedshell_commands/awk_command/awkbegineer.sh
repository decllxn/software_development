#!/bin/bash

# Author: Declan Munene
# Date: 10th June
# Description: learning the awk command



# Awk can be used to write filters
# accept standard input, then give back std output
# Automatically, awk sees the spaces as deliminaters of different fields
# syntax awk 'command' 'filename'


# printing the file
awk '{print}' tmnt.txt
