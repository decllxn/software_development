#!/bin/bash

#Taking user input
read CHARACTER

GET_CHARACTER () {
  if [[ $CHARACTER == Y || $CHARACTER == y ]]
  then
    echo YES
  else
    echo NO
  fi
}

if [[ $CHARACTER =~ [yYnN] ]]
then
  GET_CHARACTER $CHARACTER
fi
