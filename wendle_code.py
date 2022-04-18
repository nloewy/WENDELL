import numpy as np
import pandas as pd
import random
df = pd.read_csv('Survivor_Database.csv')
print(df)
answer_index = random.randint(0,len(df))
answered_first = df.iloc[answer_index]['First Name']
answered_sex = df.iloc[answer_index].values[0]
answered_tribe = df.iloc[answer_index]['Starting Tribe']
answered_placement = int(df.iloc[answer_index]['Placement'])
answered_season = int(df.iloc[answer_index]['Season'])
answered_age = int(df.iloc[answer_index]['Age'])
guess_num = 0
correct = False
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
                print((df.loc[(df['First Name']==guess_first) & (df['Season']==guess_season)]))
            elif len((df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season)])) > 1:
                print('Season', guess_season, 'Has multiple', guess_first, 'Input Last Initial:')
                guess_last = input()
                if len(df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name']== guess_last)]) == 0 :
                    print('Invalid Guess. Spell it correctly and capitalize first and last initial.')
                if len(df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name']== guess_last)]) == 1 :
                    valid_guess = True
                    guess_index = df.loc[(df['First Name']==guess_first) & (df['Season']== guess_season) & (df['Last Name']== guess_last)].index
                    print((df.loc[(df['First Name']==guess_first) & (df['Season']==guess_season)]))
            if guess_index == answer_index:
                print('CORRECT! The answer was:', df.iloc[answer_index]['Full Name'], 'From Season', df.iloc[answer_index]['Season'], 'Placement:', df.iloc[answer_index]['Placement'], 'Age', df.iloc[answer_index]['Age'], 'Starting Tribe Color', df.iloc[answer_index]['Starting Tribe'])
                print('This took you', guess_num, 'guesses!')
                correct = True
            else:
                guessed_first = df.iloc[guess_index]['First Name'].values[0]
                guessed_sex = df.iloc[guess_index]['Sex'].values[0]
                guessed_tribe = df.iloc[guess_index]['Starting Tribe'].values[0]
                guessed_placement = int(df.iloc[guess_index]['Placement'].values[0])
                guessed_season = int(df.iloc[guess_index]['Season'].values[0])
                guessed_age = int(df.iloc[guess_index]['Age'].values[0])
                print(type(answered_sex))
                if guessed_first == answered_first:
                    first_color = 'Green'
                else:
                    first_color = 'White'
                if guessed_sex == answered_sex:
                    sex_color = 'Green'
                else:
                    sex_color = 'White'
                if guessed_tribe == answered_tribe:
                    tribe_color = 'Green'
                else:
                    tribe_color = 'White'
                if guessed_season == answered_season:
                    season_color = 'Green'
                elif guessed_season - answered_season <= 2 and guessed_season - answered_season >= 0:
                    season_color = 'Yellow. Try a older season.'
                elif guessed_season - answered_season >= -2 and guessed_season - answered_season <= 0:
                    season_color = 'Yellow. Try a newer season.'
                elif guessed_season > answered_season:
                    season_color = 'White. Try a older season.'
                else:
                    season_color = 'White. Try a newer season.'  
                if guessed_age == answered_age:
                    age_color = 'Green'
                elif guessed_age - answered_age <= 2 and guessed_age - answered_age >= 0:
                    age_color = 'Yellow. Try a younger castaway.'
                elif guessed_age - answered_age >= -2 and guessed_age - answered_age <= 0:
                    age_color = 'Yellow. Try an older castaway.'
                elif guessed_age > answered_age:
                    age_color = 'White. Try a younger castaway.'
                else:
                    age_color = 'White. Try an older castaway.' 
                if guessed_placement == answered_placement:
                    placement_color = 'Green'
                elif guessed_placement - answered_placement <= 2 and guessed_placement - answered_placement >= 0:
                    placement_color = 'Yellow. Try a better placement.'
                elif guessed_placement - answered_placement >= -2 and guessed_placement - answered_placement <= 0:
                    placement_color = 'Yellow. Try a worse placement.'
                elif guessed_placement > answered_placement:
                    placement_color = 'White. Try a better placement.'
                else:
                    placement_color = 'White. Try a worse placement.' 
                print('Your Guess is:   ', df.iloc[guess_index].values[0])
                print()
                print('First Name: You Guessed:   ', df.iloc[guess_index]['First Name'].values[0], '   Color:   ', first_color)
                print()
                print('Sex: You Guessed:   ',df.iloc[guess_index]['Sex'].values[0], '   Color:   ', sex_color)
                print()
                print('Season: You Guessed:   ',df.iloc[guess_index]['Season'].values[0], '   Color:   ', season_color)
                print()
                print('Age: You Guessed:   ',df.iloc[guess_index]['Age'].values[0], '   Color:   ',age_color)
                print()
                print('Placement: You Guessed:   ',df.iloc[guess_index]['Placement'].values[0],'   Color:   ', placement_color)
                print()
                print('Starting Tribe Color: You Guessed:   ',df.iloc[guess_index]['Starting Tribe'].values[0], '   Color:    ',tribe_color)
                print()
