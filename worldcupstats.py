"""
2022 FIFA World Cup Stats Program
Developed by: Aneeb Zulfiqar and Gabriel Duran
INST 326 - Final Project
"""
import csv

import sys
import argparse

class Teams():

    """Team Class stores the data related to individual Teams

    Attributes:
        name
        goals
        ...

    """
    def __init__(self, name, goals):
        pass



#def func():
#    pass


def main(name):

    csv_file_path = "team_data.csv"

    with open(csv_file_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)



def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as
    arguments

    Args:
        args_list (list) : the list of strings from the command prompt

    Returns:
        args (ArgumentParser)
    """
        
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    parser.add_argument('xx', type=str, help='The path to the text file.') #xx team name

    args = parser.parse_args(args_list) 
    
    return args
    


if __name__ == "__main__":
    input = parse_args(sys.argv[1:])
    #print(main(input.xx))
    main(input.xx)
   