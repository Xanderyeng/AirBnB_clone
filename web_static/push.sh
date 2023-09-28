#!/bin/bash

#chmod +x *.py

# Function to make .py files executable recursively
# make_py_files_executable() {
#  for file in $(find . -type f -name "*.py"); do
#    chmod +x "$file"
#  done
# }

# Calling the function
# make_py_files_executable

git add .
git commit -m "$1"
git push
