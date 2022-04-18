import numpy as np
import pandas as pd
import random
class bcolors:
    GREEN = '\033[92m' #GREEN
    YELLOW = '\033[93m' #YELLOW
    RESET = '\033[0m' 
df = pd.read_csv('Survivor_Database.csv')
playing = True
while playing == True:
    difficulty_selected = False
    while difficulty_selected == False:
        print('Pick a difficulty level. Type E, M, or H')
        difficulty = input()
        if difficulty == 'm' or difficulty == 'M':
            guess_df = df.loc[df['Difficulty'] != 'H']
            difficulty_selected = True
        elif difficulty == 'e' or difficulty == 'E':
            guess_df = df.loc[df['Difficulty'] == 'E']
            difficulty_selected = True
        elif difficulty == 'h' or difficulty == 'H':
            guess_df = df
            difficulty_selected = True
        else:
            difficulty_selected = False
    answer_index = random.randint(0,len(guess_df))
    answered_first = guess_df.iloc[answer_index]['First Name']
    answered_full = guess_df.iloc[answer_index]['Full Name']
    answered_sex = guess_df.iloc[answer_index]['Sex']
    answered_tribe = guess_df.iloc[answer_index]['Starting Tribe']
    answered_placement = int(guess_df.iloc[answer_index]['Placement'])
    answered_season = int(guess_df.iloc[answer_index]['Season'])
    answered_age = int(guess_df.iloc[answer_index]['Age'])
    guess_num = 0
    correct = False
    column_names = ["Name", "Sex", "Season", "Age", "Placement", "Tribe"]
    my_df = pd.DataFrame(columns = column_names)
    while correct == False:
        guess_num += 1
        valid_guess = False
        print('Guess #', guess_num, 'Enter Your Guess:')
        while valid_guess == False:
            print('Guess the Players First Name')
            guess_first = input()
            print('Guess the Players Season')
            guess_season = int(input())
            if len((df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season)])) == 0:
                print('Invalid Guess. Spell it correctly and capitalize first initial.')
            else:
                if len((df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season)])==1):
                    valid_guess = True
                    guess_index = (df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season)]).index
                elif len((df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season)])) > 1:
                    print('Season', guess_season, 'Has multiple', guess_first, 'Input Last Initial:')
                    guess_last = input()
                    if len(df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name'][0]== guess_last)]) == 0 :
                        print('Invalid Guess. Spell it correctly and capitalize first and last initial.')
                    if len(df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name'][0]== guess_last)]) == 1 :
                        valid_guess = True
                        guess_index = df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name'][0]== guess_last)].index
                guessed_first = df.iloc[guess_index]['First Name'].values[0]
                guessed_sex = df.iloc[guess_index]['Sex'].values[0]
                guessed_tribe = df.iloc[guess_index]['Starting Tribe'].values[0]
                guessed_placement = int(df.iloc[guess_index]['Placement'].values[0])
                guessed_season = int(df.iloc[guess_index]['Season'].values[0])
                guessed_age = int(df.iloc[guess_index]['Age'].values[0])
                if guessed_first == answered_first and guessed_sex==answered_sex and guessed_tribe == answered_tribe and guessed_placement == answered_placement and guessed_season == answered_season and guessed_age==answered_age:
                    print(f'{bcolors.GREEN} CORRECT! The answer was: {answered_first} From Season {answered_season} Placement:  {answered_placement} Age  {answered_age} Starting Tribe Color {answered_tribe} {bcolors.RESET}')
                    print('This took you', guess_num, 'guesses!')
                    strname = f"{bcolors.GREEN}Name: {answered_first}{bcolors.RESET}"
                    strsex = f"{bcolors.GREEN}Sex: {answered_sex}{bcolors.RESET}"
                    strseason = f"{bcolors.GREEN}Season: {answered_season}{updown_season}{bcolors.RESET}"
                    strage = f"{bcolors.GREEN}Age: {df.iloc[guess_index]['Age'].values[0]}{answered_age}{bcolors.RESET}"
                    strplacement = f"{bcolors.GREEN}Placement:{answered_placement}{bcolors.RESET}"
                    strtribe = f"{bcolors.GREEN}Tribe:{answered_tribe}{bcolors.RESET}"
                    correct = True
                else:
                    if guessed_first == answered_first:
                        first_color = bcolors.GREEN
                    else:
                        first_color = bcolors.RESET
                    if guessed_sex == answered_sex:
                        sex_color = bcolors.GREEN
                    else:
                        sex_color = bcolors.RESET
                    if guessed_tribe == answered_tribe:
                        tribe_color = bcolors.GREEN
                    else:
                        tribe_color = bcolors.RESET
                    if guessed_season == answered_season:
                        season_color = bcolors.GREEN
                        updown_season = ''
                    elif guessed_season - answered_season <= 2 and guessed_season - answered_season >= 0:
                        season_color = bcolors.YELLOW
                        updown_season = ' u\u2193'
                    elif guessed_season - answered_season >= -2 and guessed_season - answered_season <= 0:
                        season_color = bcolors.YELLOW
                        updown_season = ' u\u2191'
                    elif guessed_season > answered_season:
                        season_color = bcolors.RESET
                        updown_season = 'u\u2193'
                    else:
                        season_color = bcolors.RESET
                        updown_season = ' u\u2191' 
                    if guessed_age == answered_age:
                        age_color = bcolors.GREEN
                        updown_age = ''
                    elif guessed_age - answered_age <= 2 and guessed_age - answered_age >= 0:
                        age_color = bcolors.YELLOW
                        updown_age = ' u\u2193' 
                    elif guessed_age - answered_age >= -2 and guessed_age - answered_age <= 0:
                        age_color = bcolors.YELLOW
                        updown_age = ' u\u2191' 
                    elif guessed_age > answered_age:
                        age_color = bcolors.RESET
                        updown_age = ' u\u2193' 
                    else:
                        age_color = bcolors.RESET
                        updown_age = ' u\u2191' 
                    if guessed_placement == answered_placement:
                        placement_color = bcolors.GREEN
                        updown_placement = ''
                    elif guessed_placement - answered_placement <= 2 and guessed_placement - answered_placement >= 0:
                        placement_color = bcolors.YELLOW
                        updown_placement = ' better'
                    elif guessed_placement - answered_placement >= -2 and guessed_placement - answered_placement <= 0:
                        placement_color = bcolors.YELLOW
                        updown_placement = ' worse'
                    elif guessed_placement > answered_placement:
                        placement_color = bcolors.RESET
                        updown_placement = ' better'
                    else:
                        placement_color = bcolors.RESET
                        updown_placement = ' worse'
                    print('Your Guess is: ')
                    strname = f"{first_color}Name: {df.iloc[guess_index]['Full Name'].values[0]}{bcolors.RESET}"
                    strsex = f"{sex_color}Sex: {df.iloc[guess_index]['Sex'].values[0]}{bcolors.RESET}"
                    strseason = f"{season_color}Season: {df.iloc[guess_index]['Season'].values[0]}{updown_season}{bcolors.RESET}"
                    strage = f"{age_color}Age: {df.iloc[guess_index]['Age'].values[0]}{updown_age}{bcolors.RESET}"
                    strplacement = f"{placement_color}Placement:{df.iloc[guess_index]['Placement'].values[0]}{updown_placement}{bcolors.RESET}"
                    strtribe = f"{tribe_color}Tribe:{df.iloc[guess_index]['Starting Tribe'].values[0]}{bcolors.RESET}"
                    df2 = {'Name': strname, 'Sex': strsex, 'Season': strseason, 'Age': strage, 'Placement': strplacement, 'Starting Tribe Color': strtribe}
                    my_df = my_df.append(df2, ignore_index = True)
                    print(my_df.to_string())
                    print()
                    print()
    print('Press Y to play again.')
    press_y = input()
    if press_y == 'y' or press_y == 'Y':
        playing = True
    else: 
        playing = False

