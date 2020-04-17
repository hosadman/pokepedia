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

     

    return df


def  sort_stats(df):

    df = df[['name', 'type1', 'type2', 'hp', 'attack', 'defense', 'sp_attack, 'sp_defense', 'speed']]

    print('Top 5 Pokemon with the highest attack stats:\n')  
    print(df.sort_values('attack', ascending=False).head(5))

    print('Top 5 Pokemon with the highest defense stats:\n')  
    print(df.sort_values('defense', ascending=False).head(5))

    print('Top 5 Pokemon with the highest special attack stats:\n')  
    print(df.sort_values('sp_attack', ascending=False).head(5))

    print('Top 5 Pokemon with the highest defense stats:\n')  
    print(df.sort_values('sp_defense', ascending=False).head(5))

    print('Top 5 Pokemon with the highest speed stats:\n')  
    print(df.sort_values('speed', ascending=False).head(5))


def general_stats(df):

    cols = list(df.columns.values)

    df = df[[cols[28]] + [cols[0]] + [cols[23]]]

    print('The general information of these Pokemon:\n')   
    print(df)



def main():
    while True:
        pokegen, poketype = get_input()
        df = load_data(pokegen, poketype)
        sort_stats(df)
        general_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
