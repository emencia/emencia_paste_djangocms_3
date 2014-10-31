#!/usr/bin/env python
"""
A tiny script to rename filename prefix with dot in filename prefixed with 
"+dot+" to ensure correct naming after updating Foundation5 sources

Just execute it here, and the updated sources will be ready to be committed.
"""
import os

for root, dirs, files in os.walk(os.path.dirname(__file__)):
    for name in files:
        if name.startswith('.'):
            current_path = os.path.join(root, name)
            new_name = "+dot+{0}".format(name[1:])
            new_path = os.path.join(root, new_name)
            print current_path, '=>', new_path
            # Remove previous file it it exists (this should not be)
            if os.path.exists(new_path):
                os.remove(new_path)
            # Then rename it
            os.rename(current_path, new_path)