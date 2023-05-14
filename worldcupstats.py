"""
2022 FIFA World Cup Stats Program:
This script allows users to search for statistics of all international Teams from the 2022 FIFA WC. 
Developed by: Aneeb Zulfiqar and Gabriel Duran
INST 326 - Final Project
"""
import csv
import requests
from urllib import parse
from bs4 import BeautifulSoup

class Team():
    """Team Class stores the data related to individual Teams. 
        Stores all the basic and detailed statistics.

    Attributes:
        teamName: name of the football team/country (string).
    """
    def __init__(self, teamName):
        #Basic Stats
        self.teamName = teamName
        self.group = ''
        self.games = ''
        self.goals = ''
        self.wins = ''
        self.losses = ''
        self.rank = ''
        #Detailed Stats
        self.totalPlayers = ''
        self.avgAge = ''
        self.yellowCards = ''
        self.redCards = ''
        self.fouls = ''
        self.offsides = ''
        self.ownGoals = ''
        self.shots = ''
        self.shotsonTarget = ''
        self.pensMade = ''
        self.cornersTaken = ''
        self.passesComplete = ''
        self.saves = ''


def iofunc(csv_file_teams, csv_file_groups):
    """iofunc function - Asks users for input, checks input and calls the csv handler and web parser functions
        to retrive data. Prints our the returned data.

    Parameters:
        csv_file_teams: the file path of the CSV file containg team data (string).
        csv_file_groups: the file path of the CSV file containg group data (string).
    """
    x = True
    while x == True:
        print("Select one and press Enter: \n[1] - List of All Teams\n[2] - Search Basic Team Stats\
                \n[3] - Search Detailed Team Stats\n[Q] - Quit the Program ")
        firstInput = input("> ")

        while firstInput != "1" and firstInput != "2" and firstInput != "3" and firstInput != "Q" and firstInput != "q" :
                print("Please enter either 1, 2, 3 or Q.")
                firstInput = input("> ")
        if firstInput == 'Q' or firstInput == 'q':
            print("Program Quit.")
            exit()
        if firstInput == "1":
            csv_handler(csv_file_teams, csv_file_groups, firstInput)
        elif firstInput == "2":
            print("Enter a Team Name. I.E:  Qatar :")
            teamInput = input("> ")
            while not csv_handler(csv_file_teams, csv_file_groups, teamInput):
                teamInput = input("Please enter a valid Team Name. I.E: Qatar: \n")
            teamData = csv_handler(csv_file_teams, csv_file_groups, teamInput)

            print("\nTeam Entered:", teamData.teamName )
            print("Historical WC Wins:", web_parser(teamInput))
            print("2022 WC Group:", teamData.group)
            print("Total Matches:", teamData.games)
            print("Group Wins:",teamData.wins)
            print("Group Losses:", teamData.losses)
            print("Total Goals:", teamData.goals)
            print("Group Rank:", teamData.rank)
            print("")

            print("Would you like to create a text file with this Data? (Y or N):")
            fileInput = input("> ")
            while fileInput != "Y" and fileInput != "N" and fileInput != "y" and fileInput != "n":
                fileInput = input("Please only enter Y or N: \n")
            if fileInput == "Y" or fileInput == "y":
                file_output(teamData, "Basic")
            else: continue

        elif firstInput == "3":
            print("Enter a Team Name. I.E:  Qatar :")
            teamInput = input("> ")
            while not csv_handler(csv_file_teams, csv_file_groups, teamInput):
                teamInput = input("Please enter a valid Team Name. I.E: Qatar: \n")
            teamData = csv_handler(csv_file_teams, csv_file_groups, teamInput)

            print("\nTeam Entered:", teamData.teamName )
            print("Historical WC Wins:", web_parser(teamInput))
            print("2022 WC Group:", teamData.group)
            print("Total Matches:", teamData.games)
            print("Group Wins:",teamData.wins)
            print("Group Losses:", teamData.losses)
            print("Total Goals:", teamData.goals)
            print("Group Rank:", teamData.rank)
            print("Total Players:", teamData.totalPlayers)
            print("Avg. Player Age:", teamData.avgAge)
            print("Yellow Cards:", teamData.yellowCards)
            print("Red Cards:",teamData.redCards)
            print("Fouls:", teamData.fouls )
            print("Offsides:", teamData.offsides)
            print("Own Goals:", teamData.ownGoals)
            print("Total Shots:", teamData.shots)
            print("Shots on Target:",teamData.shotsonTarget)
            print("Pens Made:", teamData.pensMade)
            print("Corners Taken:", teamData.cornersTaken)
            print("Passes Complete:", teamData.passesComplete)
            print("Total Saves:",teamData.saves)
            print("")

            print("Would you like to create a text file with this Data? (Y or N):")
            fileInput = input("> ")
            while fileInput != "Y" and fileInput != "N" and fileInput != "y" and fileInput != "n":
                fileInput = input("Please only enter Y or N: \n")
            if fileInput == "Y" or fileInput == "y":
                file_output(teamData, "Det")
            else: continue

def csv_handler(csv_file_teams, csv_file_groups, userInput):
    """csv_handler function - Takes in input from the iofunc and finds the data in specified CSV file.
        
    Parameters:
        csv_file_teams: the file path of the CSV file containg team data (string)
        csv_file_groups: the file path of the CSV file containg group data (string)
        userInput: input from users sent from iofunc (string)
    Returns:
        A tuple with Team objects that contains data.
    """
    
    with open(csv_file_teams, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
         
        if userInput == "1":
            for row in csv_reader:
                print(row[0])
            print("")
        else:
             for row in csv_reader:
                if  userInput == row[0]:
                    team = Team(userInput)
                    team.totalPlayers = row[1]
                    team.avgAge = row[2]
                    team.yellowCards = row[13]
                    team.redCards = row[14]
                    team.fouls = row[179]
                    team.offsides = row[181]
                    team.ownGoals = row[184]
                    team.shots = row[70]
                    team.shotsonTarget = row[71]
                    team.pensMade = row[11]
                    team.cornersTaken = row[110]
                    team.passesComplete = row[82]
                    team.saves = row[35]
                    team.goals = row[8]
                    team.games = row[4]
                    with open(csv_file_groups, 'r') as csv_file:
                        csv_reader = csv.reader(csv_file)
                        for row in csv_reader:
                            if userInput == row[3]:
                                if row[1] == '1': team.group = 'A' 
                                if row[1] == '2': team.group = 'B'
                                if row[1] == '3': team.group = 'C'
                                if row[1] == '4': team.group = 'D'
                                if row[1] == '5': team.group = 'E'
                                if row[1] == '6': team.group = 'F'
                                if row[1] == '7': team.group = 'G'
                                if row[1] == '8': team.group = 'H'
                            team.wins= row[5]
                            team.losses = row[7]
                            team.rank = row[2]
                    return(team)


def web_parser(userInput):
    """web_parser function - Uses a webpage to scrape the historical wins of all teams.

        Returns: The number of wins the entered Team has (string).
    """
    url ='https://en.wikipedia.org/wiki/List_of_FIFA_World_Cup_finals'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    caption = soup.find_all('caption')
    table = soup.find_all('table')

    for words in caption:
        if words.text == "Results by nation\n":
            table = words.parent
            teams = table.find_all('a', title=lambda x: x and 'national football team' in x)
            trophies = table.find_all('td', attrs={'align': lambda value: value != 'left'})
            teamsList = []
            numStatsList = []
            winsList = []
            
            for x in teams:
                #print(x.text)
                teamsList.append(x.text)
            for y in trophies:
                #print(y.text)
                numStatsList.append(y.text) 

    statsSliced = numStatsList[0:24]
    winsList = statsSliced[0::3]
    teamWinsDict = {}

    for i in range(len(teamsList[0:8])):
        teamWinsDict[teamsList[i]] = winsList[i]

    for key in teamWinsDict:
        if userInput in key:
            #print(teamWinsDict)
            win = teamWinsDict[key]
            return win.strip()
    else: return '0'

def file_output(teamData, dataAmount):
    """
    file_output function - Creates a Text file for the team and with the amount of Data that the user specified.

    Paramters:
        teamData: A Team Object containg all the attributes of the team the user chose.
        dataAmount: specifies the amoount of data. Det = Detailed amd Basic= Basic (string).
    """
    TeamName = teamData.teamName

    if dataAmount == "Det":
        with open(f"2022_WC_{TeamName}_Stats.txt", "w") as file:
            file.write(f"2022 FIFA World Cup Stats for: {TeamName}\n")   
            file.write("")
            file.write(f"\nHistorical WC Wins: {web_parser(TeamName)}")
            file.write(f"\n2022 WC Group: {teamData.group}")
            file.write(f"\nTotal Matches: {teamData.games}")
            file.write(f"\nGroup Wins: {teamData.wins}")
            file.write(f"\nGroup Losses: {teamData.losses}")
            file.write(f"\nTotal Goals: {teamData.goals}")
            file.write(f"\nGroup Rank: {teamData.rank}")
            file.write("")
            file.write(f"\nTotal Players: {teamData.totalPlayers}")
            file.write(f"\nAvg. Player Age: {teamData.avgAge}")
            file.write(f"\nYellow Cards: {teamData.yellowCards}")
            file.write(f"\nRed Cards: {teamData.redCards}")
            file.write(f"\nFouls: {teamData.fouls}")
            file.write(f"\nOffsides: {teamData.offsides}")
            file.write(f"\nOwn Goals: {teamData.ownGoals}")
            file.write(f"\nTotal Shots: {teamData.shots}")
            file.write(f"\nShots on Target: {teamData.shotsonTarget}")
            file.write(f"\nPens Made: {teamData.pensMade}")
            file.write(f"\nCorners Taken: {teamData.cornersTaken}")
            file.write(f"\nPasses Complete: {teamData.passesComplete}")
            file.write(f"\nTotal Saves: {teamData.saves}")
            file.write("")
            file.close()
            print("File Created With Detailed Info.\n")
    if dataAmount == "Basic":
        with open(f"2022_WC_{TeamName}_Stats.txt", "w") as file:
            file.write(f"2022 FIFA World Cup Stats for: {TeamName}.\n")   
            file.write("")
            file.write(f"\nHistorical WC Wins: {web_parser(TeamName)}")
            file.write(f"\n2022 WC Group: {teamData.group}")
            file.write(f"\nTotal Matches: {teamData.games}")
            file.write(f"\nGroup Wins: {teamData.wins}")
            file.write(f"\nGroup Losses: {teamData.losses}")
            file.write(f"\nTotal Goals: {teamData.goals}")
            file.write(f"\nGroup Rank: {teamData.rank}")
            file.write("")
            print("File Created With Basic Info.\n")

def main():
    """
    main function - Calls the iofunc (input/output fuction) with the CSV file names.
    """
    csv_file_teams = "team_data.csv"
    csv_file_groups = "group_stats.csv"
    iofunc(csv_file_teams, csv_file_groups)


if __name__ == "__main__":
   main()
