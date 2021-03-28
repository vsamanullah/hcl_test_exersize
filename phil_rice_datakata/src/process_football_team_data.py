'''system imports'''
import argparse
import re

''' match
This function function prints the name of the team the smallest difference in ‘for’ and ‘against’ goals
Open the football input data files , scan the lines with valid format.
for the valid formats it calculates difference in goal
Then prints list diff name

'''

def print_team_least_diff_in_football_goals(team_data_file):
    file_lines = parse_football_data(team_data_file)
    valid_lines = list_only_valid_lines(file_lines)
    team_diff_goals_dict = find_diff_goals_and_construct_dict(valid_lines)
    least_diff_in_goal = ''
    if team_diff_goals_dict:
        least_diff_in_goal = find_team_least_diff_in_goal(team_diff_goals_dict)
    print(least_diff_in_goal)

'''
Read the entire file in to the string
'''
def parse_football_data(team_data_file):
    #read the complete file in to a string
    with open(team_data_file) as file_handle:
        file_lines = file_handle.read()
    return file_lines

'''
This function checks if each line of data is in valid format , 
if so return name , goal for and against
'''
def list_only_valid_lines(file_lines):
    # this regex is looks for format   20. Leicester       38     5  13  20    30  -  64    28
    # returns : team name for goal , against goal [('Arsenal', '79', '36'), ('Liverpool', '67', '30')
    football_data_regex = re.compile(r'\s*\d+\.\s*(.*?)\s+\d+\s+\d+\s+\d+\s+\d+\s+(\d+)\s+-\s+(\d+)\s+\d+.')
    return re.findall(football_data_regex,file_lines)

'''
this function iterates and calculate the diff between goal and 
create a dict with key as diff and values as list of teams
'''
def find_diff_goals_and_construct_dict(valid_team_data_list):
    team_diff_goals_dict = {}
    for each_data in valid_team_data_list:
        key_for_dict = abs(int(each_data[1]) - int(each_data[2]))
        if key_for_dict in team_diff_goals_dict:
            team_diff_goals_dict[key_for_dict].append(each_data[0])
        else:
            team_diff_goals_dict[key_for_dict] = [(each_data[0])]
    return team_diff_goals_dict


'''
sort the dict based on the key
then access only the team names from the dict , always the first elem is with low goals
construct a string of team seperated by ,
'''
def find_team_least_diff_in_goal(team_diff_goals_dict):
    # sort the dict based on the key
    list_from_sorted_dict_based_on_key = sorted(team_diff_goals_dict.items(), key=lambda kv: (kv[0], kv[1]))
    #then access only the team names from the dict , always the first elem is with low goals
    list_of_teams_with_least_goal_diff = list_from_sorted_dict_based_on_key[0][1]
    # remove the duplicates from the list
    list_of_teams_with_least_goal_diff = list(dict.fromkeys(list_of_teams_with_least_goal_diff))
    #construct a string of team seperated by ","
    return ",".join(sorted(list_of_teams_with_least_goal_diff))

if __name__ == '__main__':
    # Command line arguments
    parser = argparse.ArgumentParser(description='print the name of the team with the smallest difference in ‘for’ and ‘against’ goals')
    parser.add_argument("-i", "--input_file", type=str, help="input file used for calculating smallest difference in ‘for’ and ‘against’ goals",
                        default="..//input_data//football.dat")
    args = parser.parse_args()
    print("args: " + str(args))
    print_team_least_diff_in_football_goals(args.input_file)