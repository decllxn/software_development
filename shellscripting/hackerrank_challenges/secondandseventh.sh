#!/bin/bash

# Author: Declan Munene
# Date: 4/05/2024
# This script takes inputs from users and prints the third and seventh character of each string

# Array to store strings
string_arr=()

# Function to get strings from the user
function GET_INPUTS () {
    read INPUTS
    if [ -z "$INPUTS" ]; then
      return 0
    else
      string_arr+=("$INPUTS") #Appending inputs to array
      GET_INPUTS
    fi    
}

# Get strings from the user
GET_INPUTS

# Array to store second characters of each string
second_arr=()
# Array to store seventh characters of each string
seventh_arr=()

# Loop through the input strings to extract the second and seventh characters
for str in "${string_arr[@]}" 
do
  second_arr+=("${str:1:1}") # Second character appended
  seventh_arr+=("${str:6:1}") # Seventh character appended
done

# Print the second and seventh characters of each string
for (( i = 0; i < ${#string_arr[@]}; i++ )) # Loop through the indices
do
  echo "${second_arr[i]}${seventh_arr[i]}"
done
