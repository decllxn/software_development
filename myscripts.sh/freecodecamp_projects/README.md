##The following are learning projects from free code camp
##Questionnaire project
  -Emphasis was on how to create variables, how to accept user input and store them in specific variables
  -This is also where I learnt if statements for bash
  if [[ boolean expression ]]
  then
    expression 1
  elif
    expression 2
  else
    expression 3
  fi

##Countdown project
  - I learnt how to use for and while loops to iterate through data
  - I also learnt how to pass arguments to scripts ./<file-name> argument1 argument2..
  - for loops
  - for (( initialization; boolean expression; finalization ))
    do
      expression
    done
  - while (( boolean expression ))
    do
      expression
    done
##bingo project
  - I learnt that in bash to evaluate expressions is different for square brackets and for parenthises
  - For square brackets
    You need to prepend variables using $
    you need to use flags such as -lt(for less than), ge(greater than or equal to)
  - For parenthesis
    You do not need to prepend variables
    You use expressions operater >=(greater than or equal to)
  - Example. Show an expresson that checks if a variable I is greater than 15
    [[ $I -gt 15 ]]
    (( I > 15 ))
  - I also learnt how to generate random numbers using RANDOM variable
    
