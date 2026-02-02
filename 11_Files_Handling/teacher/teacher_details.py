import os, sys

from os.path import dirname, join, abspath

parent_dir_path = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, parent_dir_path)

from Student import student_details

def teacher():
    print("This are the teacher details")
student_details.student()