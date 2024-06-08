#!/bin/bash

# Author: Declan Munene
# Date: 8/6/2024
# Project: To do list app
# Description: a simple to-do list application, 
#              where users can add, remove, and mark tasks 
#              as complete.


# Taking user input, using read -p and saves input to a variable
read -p "Enter the file name: " TASK_FILE


# Function to create file
create_file() {
    local $TASK_FILE="$1"
    touch "$TASK_FILE"

    echo "File '$TASKFILE' created successfully."
 }

# Function to check if task file exists
# I use if [ -flag "filename" ]

doesTaskFileExist() {
    if [ -f "$TASK_FILE" ]; then # Checks if the file exists
        if [ -s "$TASK_FILE" ]; then # checks if the is empty
            echo "Today's To-Do list"
            nl -w2 -s'. ' "$TASK_FILE"
        else
            echo "$TASK_FILE exists but is empty."
        fi
    else
        read $TASK_FILE
        create_file "$TASK_FILE"
    fi
}

# Function to add a task to the task file

append_task() { # function, that takes two parameters
    local task="$1" # local kw = to define the parameters the tasks require
    local file="$TASK_FILE" # takes the task file as a parameter 
    
    echo "$task" >> "$file"
    echo "Task added to $file"
}

# Function to remove a specified task
# We use the sed command
# SED command = "stream editor"

# used for parsing or transforming text
# It is commonly used for performing operations such as
# Searching, replacing, inserting and deleting

# Search and replace
# sed 's/old_text/new_text/g' file.txt

# Delete lines
# sed '/pattern_to_delete/d' file.txt

# Insert lines
# sed 'pattern_to_insert/i\new_line_to_insert' file.txt

# Regex
# sed -E 's/[0-9]+/number/g' file.txt


remove_task () {
    sed -i "${1}d" "$TASK_FILE"
    echo "Task number $1 removed."
}

# Implementing while loop to continously display the menu until the user chooses not to
# using a case statement to handle user options

while true
do
    echo ""
    echo "To-Do List App"
    echo "1. Add Task"
    echo "2. Remove Task"
    echo "3. Display Tasks"
    echo "4. Exit"
    read -p "Enter your choice: " choice

    case $choice in
    1)
       read -p "Enter the task: " task
       append_task "$task" "$TASK_FILE"
       ;;
    2)
       doesTaskFileExist
       read -p "Enter the task number to remove: " task_number
       remove_task "$task_number"
       ;;
    3)
       doesTaskFileExist
       ;;
    4)
       echo "Exiting the app. Have a good day!"
       exit 0
       ;;
    *)
       echo "Invalid choice. Please try again."
       ;;
    esac      
done
