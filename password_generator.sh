#!/bin/bash

# I KNOW PASSWORDS ARE KIND OF PASS FOR OPESEC, BUT THIS COULD BE USED
# AS A TEMP WAY FOR THOSE WANTING TO ACCESS THEIR ACCOUNTS IN THE EVENT SOMETHING GOES SOUTH.
# YOU NEVER REALLY KNOW

# Function to generate a random password
generate_password() {
    # Read 16 bytes from /dev/urandom
    # Convert to base64 and strip out non-alphanumeric characters
    PASSWORD=$(head -c 16 /dev/urandom | base64 | tr -dc 'a-zA-Z0-9')

    # Output the password
    echo "Generated password: $PASSWORD"
}

# Call the function to generate a password
generate_password
