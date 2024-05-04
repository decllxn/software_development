#!/bin/bash
# This script computes (N) number of integers, rounded to 3 decimal places
# First line computes N number of integers to be computed
# Each of the following lines contains the integers themselves
# 1 <= N <= 500
# Integers (x) given should be -10000 <= x <= 10000
# If the user enters N = 4, the script should only accept 4 integers

# Getting N number of inputs
read N
number_array=()

GET_INPUTS() {
  read userInput
  if [ ${#number_array[@]} -eq $N ]; then
    return 0
  else
    # Check if input is numeric and within range
    if [[ $userInput =~ ^[0-9]+([.][0-9]+)?$ && $userInput -ge -10000 && $userInput -le 10000 && $userInput != 0 ]]; then
      number_array+=("$userInput")
    else
      echo "Invalid input. Please enter a number between -10000 and 10000."
    fi
    GET_INPUTS
  fi
}

GET_AVERAGE() {
  sum=0
  for num in "${number_array[@]}"; do
    sum=$(bc <<< "$sum + $num")
  done

  # Calculating the average
  average=$(bc <<< "scale=3; $sum / ${#number_array[@]}")
  rounded=$(printf "%.3f" $average)
  echo $rounded
}

GET_INPUTS
GET_AVERAGE

