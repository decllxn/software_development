#!/bin/bash

#creating 100 dash columns and 63 dash rows
DASH="-"
for (( i=0; i <= 100; i++ )); do
  for (( j=0; j <=63; j++ )); do
    echo -n $DASH
  done
  echo ""
done
  
