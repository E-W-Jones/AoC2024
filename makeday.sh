#!/bin/bash

# Generate for a user input X the following file structure:
# Day X
# ├── dayX.py
# ├── sample_input.py
# └── input.txt

printf -v N "%02d" $1
DIR="Day $N"

mkdir "$DIR"
touch "$DIR/sample_input.txt"
touch "$DIR/input.txt"
touch "$DIR/day$N.py"