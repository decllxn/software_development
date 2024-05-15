#!/bin/bash

# Author: Declan Munene
# Date: 4/05/2024
# This script takes strings from the user until there's no input, extracts the third character of each string, and prints them.

# Array to store strings
string_arr=()
third_char=()

# Function to get strings from the user
function GET_STRING () {
    read INPUT
    if [ -z "$INPUT" ]; then
        return 0
    else
        string_arr+=("$INPUT")  # Append input to array
        GET_STRING
    fi
}

# Call function to get strings
GET_STRING

# Extract the third character of each string
for str in "${string_arr[@]}"
do
    third_char+=("${str:2:1}")  # Append the third character to third_char array
done

# Print each third character on a new line
for char in "${third_char[@]}"
do
    echo "$char"
done
