#!/bin/bash

# Author: Declan Munene
# Date: 6/05/2024
# This script takes inputs form user and displays a range of characters starting form the second character to the seventh

#Taking user input
string_arr=()

function GET_INPUTS () {
    read INPUTS
    if [ -z "$INPUTS" ]; then
      return 0
    else
      string_arr+=("$INPUTS")
      GET_INPUTS
    fi
}

#Calling the function
GET_INPUTS

#declaring arrays to store respective characters
second_arr=()
third_arr=()
fourth_arr=()
fifth_arr=()
sixth_arr=()
seventh_arr=()

#appending the characters to the array

for str in "${string_arr[@]}"
do
  second_arr+=("${str:1:1}")
  third_arr+=("${str:2:1}")
  fourth_arr+=("${str:3:1}")
  fifth_arr+=("${str:4:1}")
  sixth_arr+=("${str:5:1}")
  seventh_arr+=("${str:6:1}")
done

for (( i = 0; i < ${#string_arr[@]}; i++ ))
do
  echo "${second_arr[i]}${third_arr[i]}${fourth_arr[i]}${fifth_arr[i]}${sixth_arr[i]}${seventh_arr[i]}"
done