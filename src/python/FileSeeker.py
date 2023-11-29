#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 12:07:21 2021

RESUME : File Finder with Highlighted Search Word.
    
Version: v01 beta

@author: Jean Gomes Copyright (c)

@email: antineutrinomuon@gmail.com

Written: Jean Michel Gomes © Copyright
"""

# import libraries
import os
from termcolor import colored

class FileSeekerClass():
    '''FileSeekerClass is the class for fileseeker'''
    def __init__(self,search_file,search_dir='./'):
        self.search_dir   = search_dir
        self.search_file  = search_file

        self.seeker_files = self.find_files_with_name(
                                                       self.search_dir,
                                                       self.search_file
                                                     )

        if self.seeker_files:
            print("Files found:")
            for file_path in self.seeker_files:
                # Highlight search_file in color
                highlighted_path = file_path.replace(search_file,
                                   colored(search_file, 'red'))
                print(highlighted_path)
        else:
            highlighted_path = search_file.replace(search_file,
                               colored(search_file, 'red'))
            print(f"No files with the name '{highlighted_path}'"
                  f"found in the directory '{self.search_dir}'.")

    # Function to search for files with a given name in a \
    # directory and its subdirectories
    def find_files_with_name(self,directory, search_word):
        '''Find files with name or part of name'''
        found_files = []

        for root, _, files in os.walk(directory):
            for file in files:
                if search_word in file:
                    file_path = os.path.join(root, file)
                    found_files.append(file_path)

        return found_files

    def simpletest(self):
        '''Simple example of how to use'''
        # Directory to search in local
        search_directory = "./"
        # Search a given word or part of word
        search_word = "libcfiletype"
        r_object = FileSeekerClass( search_word,
                                   search_dir=search_directory )
        print(r_object.seeker_files)

def main():
    '''Main code'''
    print("")
