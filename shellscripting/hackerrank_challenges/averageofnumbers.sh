#!/bin/bash

# Getting multiple inputs until user stops
GET_INPUTS() {
  read -p "Enter an integer or press enter: " userInput
  if [ -z "$userInput" ]; then
    return 0
  else
    # Check if input is numeric and within range
    if [[ $userInput =~ ^[0-9]+([.][0-9]+)?$ && $userInput -ge -1000 && $userInput -le 1000 ]]; then
      number_array+=("$userInput")
    else
      echo "Invalid input. Please enter a number between -1000 and 1000."
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
  echo "Average: $rounded"
}

number_array=()
GET_INPUTS
GET_AVERAGE

