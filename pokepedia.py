import time
import pandas as pd
import numpy as np


def get_input():
    
    print('Hello and welcome to PokePedia! Let\'s explore the wonderful world of Pokemon!')
    
    pokegen = input('Enter any desired generation from 1-7 whose Pokemon you wish to explore\n(type "all" if you wish to see all"):\n').lower()
    poketype = input('Enter any Pokemon type whose data you wish to explore\n(type "all" if you wish to see all"):\n').lower()
    
    print('-'*20)
    return pokegen, poketype


def load_data(pokegen, poketype):
    
    df = pd.read_csv('pokemon.csv')

    if pokegen != 'all':
        pokegen = int(pokegen)
        df = df[df['generation'] == pokegen]
    
    if poketype != 'all':
        df = df[(df['type1'] == poketype) | (df['type2'] == poketype)]

    cols = list(df.columns.values)

    df = df[cols[0:19] + cols[20:25] + cols [26:33] + [cols[19]] + [cols[25]] + cols[33:]]    

    df = df.iloc[:, -13:-3]

    return df


def main():
    while True:
        pokegen, poketype = get_input()
        df = load_data(pokegen, poketype)
        print(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
