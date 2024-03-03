#!/bin/bash

# Check if ImageMagick is installed
if ! command -v convert &> /dev/null; then
    echo "Error: ImageMagick is not installed. Please install it before running this script."
    exit 1
fi

# Check if at least one argument is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <directory> <height>"
    exit 1
fi

# Check if the provided directory exists
directory="$1"
if [ ! -d "$directory" ]; then
    echo "Error: Directory '$directory' does not exist."
    exit 1
fi

# Extract height from argument
height="$2"

# Loop through JPEG files in the directory and convert them to EPS
for file in "$directory"/*.jpg; do
    if [ -f "$file" ]; then
        filename=$(basename -- "$file")
        filename_without_extension="${filename%.*}"
        eps_file="$directory/$filename_without_extension.eps"
        
        # Convert JPEG to EPS with fixed height and auto width
        echo "Converting $file to $eps_file with height $height"
        convert "$file" -resize "x$height" -set filename: "%t" -background white -flatten "$eps_file"
        
        if [ $? -eq 0 ]; then
            echo "Conversion successful"
        else
            echo "Conversion failed"
        fi
    fi
done