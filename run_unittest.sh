#!/usr/bin/env bash

# Add `__init__.py` inside each directory for test to work.

clear_pycache() {
    find ./ -regex '^.*\(__pycache__\|\.py[co]\)$' -delete
}

clear_pycache
python3 -m unittest discover -p "*_test.py" -v 
clear_pycache