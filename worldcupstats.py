"""
2022 FIFA World Cup Stats Program
Developed by: Aneeb Zulfiqar and Gabriel Duran
INST 326 - Final Project
"""
import csv
import sys
import re
import requests
from urllib import parse
from bs4 import BeautifulSoup


class Team():

    """Team Class stores the data related to individual Teams

    Attributes:
        teamName: name of the football team/country (string)

    """
    def __init__(self, teamName):
        self.teamName = teamName



#gabe
def iofunc(csv_file_teams, csv_file_groups):
    """iofunc function - Asks users for input, checks input and calls the csv handler function
        to retrive data.

    Parameters:
        csv_file_teams: the file path of the CSV file containg team data (string)
        csv_file_groups: the file path of the CSV file containg group data (string)
    Returns:
        A tuple with Team objects contains data.
    
    """
    print("Select one and press Enter: \n[1] - List of All Teams\n[2] - Search Teams ")
    firstInput = input("> ")

    while firstInput != "1" and firstInput != "2":
            print("Please enter either 1 or 2.")
            firstInput = input("> ")
    
    if firstInput == "1":
        csv_handler(csv_file_teams,csv_file_groups, firstInput)
    else:
        print("Enter a Team Name. I.E:  Qatar :")
        teamInput = input("> ")
        while not csv_handler(csv_file_teams,csv_file_groups, teamInput):
            teamInput = input("Please enter a valid Team Name. I.E: Qatar: \n")
        teamData = csv_handler(csv_file_teams,csv_file_groups, teamInput)
        return teamData


#aneeb
def csv_handler(csv_file_teams, csv_file_groups, userInput):
    """csv_handler function - Takes in input from the iofunc and finds the data in specified CSV file.
        

    Parameters:
        csv_file_teams: the file path of the CSV file containg team data (string)
        csv_file_groups: the file path of the CSV file containg group data (string)
        userInput: input from users sent from iofunc (string)
    Returns:
        A tuple with Team objects contains data
    
    """
 
    with open(csv_file_teams, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
         
        if userInput == "1":
            for row in csv_reader:
                print(row[0])
        else:
             for row in csv_reader:
                if  userInput == row[0]:
                    team = Team(userInput)
                    team.games =  row[4]
                    return(team.teamName, team.games)
           
"""
#work in progress
def web_parser():
    url ='https://en.wikipedia.org/wiki/2022_FIFA_World_Cup'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    #h3 id="Group
    groups = soup.find_all('span', id=lambda x: x and 'Group_' in x)

    for group in groups:
        print(group.text)
"""

def main():
    """main function - Calls the iofunc (input/output fuction) and prints out the data.

    
    """
    csv_file_teams = "team_data.csv"
    csv_file_groups = "group_stats.csv"
    teamData = iofunc(csv_file_teams, csv_file_groups)
    print("\nTeam Entered:", teamData[0])
    print("Total WC Wins:")
    print("2022 WC Group:")
    print("Games Played:", teamData[1])
    print("Wins:")
    print("Losses:")
    print("Goals:")
    print("Group Rank:")
    print("Final Rank:")




if __name__ == "__main__":
   main()

