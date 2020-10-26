#!/bin/sh

# Adds "noted" alias to shell
echo " " >> ~/.bash_profile
echo "# Alias for Noted application" >> ~/.bash_profile
echo "alias noted=\"python3 $(pwd)/noted.py\"" >> ~/.bash_profile
