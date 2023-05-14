"""
This script tests the web_parser and csv_handler functions from the worldcupstats.py script.
"""
from worldcupstats import Team
from worldcupstats import csv_handler
from worldcupstats import web_parser

def test_web_parser():
    """ This is a unit test to ensure the web_parser function will show the correct corresponding info for any team entered.
        The web parsing function gathers data on each team's historic wins. These are the correct stats for the 
        2022 World Cup. No assertion error is raised if the function collects accurate data through web scraping.

    """
    assert web_parser("Brazil") == "5"
    assert web_parser("Germany") == "4"
    assert web_parser("Italy") == "4"
    assert web_parser("Argentina") == "3"
    assert web_parser("France") == "2"
    assert web_parser("Uruguay") == "2"
    assert web_parser("England") == "1"
    assert web_parser("Spain") == "1"
    assert web_parser("Australia") == "0"
    assert web_parser("Qatar") == "0"
    print("web_parser test cases passed.")


def test_csv_handler():
    """ This is a unit test to make sure the csv_handler function will show the correct corresponding info for any team entered.
        The first test case checks if the csv_handler function returns the expected Team object for a valid team name ("Germany").
        It compares each attribute of the returned Team object with the expected values.
        The second test case checks if the csv_handler function returns None for an invalid team name ("Invalid Team").
        After running the test_csv_handler function, it will print a message indicating whether the test cases passed or not.

    """
    csv_file_teams = "team_data.csv"
    csv_file_groups = "group_stats.csv"
    user_team_input = "Germay"

    # Test case 1: Valid team name
    team_input = "Germany"
    expected_team_data = Team("Germany")
    expected_team_data.totalPlayers = "20"
    expected_team_data.avgAge = "28.1"
    expected_team_data.yellowCards = "3"
    expected_team_data.redCards = "0"
    expected_team_data.fouls = "26"
    expected_team_data.offsides = "12"
    expected_team_data.ownGoals = "0"
    expected_team_data.shots = "68"
    expected_team_data.shotsonTarget = "23"
    expected_team_data.pensMade = "1"
    expected_team_data.cornersTaken = "25"
    expected_team_data.passesComplete = "1686"
    expected_team_data.saves = "8"
    expected_team_data.goals = "6"
    expected_team_data.games = "3"
    expected_team_data.group = "E"
    expected_team_data.wins = "1"
    expected_team_data.losses = "2"
    expected_team_data.rank = "4"

    team_data = csv_handler(csv_file_teams, csv_file_groups, team_input)

    assert team_data.teamName == expected_team_data.teamName, "Please Enter a name that was in 2022 World Cup"
    assert team_data.totalPlayers == expected_team_data.totalPlayers, "Should be same Value from CSV file"
    assert team_data.avgAge == expected_team_data.avgAge, "Should be same Value from CSV file"
    assert team_data.yellowCards == expected_team_data.yellowCards, "Should be same Value from CSV file"
    assert team_data.redCards == expected_team_data.redCards, "Should be same Value from CSV file"
    assert team_data.fouls == expected_team_data.fouls, "Should be same Value from CSV file"
    assert team_data.offsides == expected_team_data.offsides, "Should be same Value from CSV file"
    assert team_data.ownGoals == expected_team_data.ownGoals, "Should be same Value from CSV file"
    assert team_data.shots == expected_team_data.shots, "Should be same Value from CSV file"
    assert team_data.shotsonTarget == expected_team_data.shotsonTarget, "Should be same Value from CSV file"
    assert team_data.pensMade == expected_team_data.pensMade, "Should be same Value from CSV file"
    assert team_data.cornersTaken == expected_team_data.cornersTaken, "Should be same Value from CSV file"
    assert team_data.passesComplete == expected_team_data.passesComplete, "Should be same Value from CSV file"
    assert team_data.saves == expected_team_data.saves, "Should be same Value from CSV file"
    assert team_data.goals == expected_team_data.goals, "Should be same Value from CSV file"
    assert team_data.games == expected_team_data.games, "Should be same Value from CSV file"
    assert team_data.group == expected_team_data.group, "Should be same Value from CSV file"
    assert team_data.wins == expected_team_data.wins, "Should be same Value from CSV file"
    assert team_data.losses == expected_team_data.losses, "Should be same Value from CSV file"
    assert team_data.rank == expected_team_data.rank, "Should be same Value from CSV file"

    # Test case 2: Invalid team name
    team_input = "Invalid Team"
    team_data = csv_handler(csv_file_teams, csv_file_groups, team_input)
    assert team_data is None

    print("csv_handler test cases passed.")


#Run the test function
if __name__ == "__main__":
    test_web_parser()
    test_csv_handler()
