#importing teacher_details module from teacher package
#from teacher import teacher_details # but system doesn't know the directory of teacher package and module so we need to import os

import os, sys

# generic use from wherever you want to import something from modules/packages
# os - provides functionality to interact with operation system
# sys - provides access to system specific parameters and function such as python path 

from os.path import dirname, join, abspath

#__file__ - gives path to current script, examples: this script is at d:\IMP Documents\Coding Practice\Data Analyst -PW class\Data Analyst - PW Class - Vs code\Data-Analyst-Tutorials\11_Files_Handling\Student\student_details.py
#print("The path to script", __file__)

#print("The path to script", dirname(__file__))
# dirname - will give the directory containing the curerent script
#example - dir(__file__) - d:\IMP Documents\Coding Practice\Data Analyst -PW class\Data Analyst - PW Class - Vs code\Data-Analyst-Tutorials\11_Files_Handling\Student

#print("The path to script", join(dirname(__file__), ".."))
## join(dirname(__file__), "..") - move one directory up from the current script directory -- d:\IMP Documents\Coding Practice\Data Analyst -PW class\Data Analyst - PW Class - Vs code\Data-Analyst-Tutorials\11_Files_Handling\Student\..

# print("The path to script", abspath(join(dirname(__file__), "..")))
## abspath(join(dirname(__file__), "..") converts the relative path to absolute path - d:\IMP Documents\Coding Practice\Data Analyst -PW class\Data Analyst - PW Class - Vs code\Data-Analyst-Tutorials\11_Files_Handling

parent_dir_path = abspath(join(dirname(__file__), ".."))
sys.path.insert(0, parent_dir_path)

## at index 0, add this directory to the beginning of module search/system path
## It allows to search modules and packages

# from teacher import teacher_details  ## comment this cause calling student module and can't call both at the same time thats not the best practice to do it
def student():
    print("These are student details")
# teacher_details.teacher()  # calling the module  ## ## comment this cause calling student module and can't call both at the same time thats not the best practice to do it

## __pychache__ also known as pyc files - These are compiled python files - source code to byte code. - stored in .pyc file inside __pycache__directory
## This helps up to speed up the loading the module next time it is imported