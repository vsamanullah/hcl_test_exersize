'''
system imports
'''
import sys
import os

'''
creates a directory at the given path
'''
def create_directory(directory_path_and_name):
    if not os.path.exists(directory_path_and_name):
        os.mkdir(directory_path_and_name)
        print("Directory ", directory_path_and_name, " Created ")
    else:
        print("Directory ", directory_path_and_name, " already exists")