import time
import pandas as pd
import numpy as np


def first_input():
    print('')
    print('')
    print('Hello and welcome to PokePedia! Let\'s explore the wonderful world of Pokemon!')
    print('')
    print('*'*20)
    print('')

    search = input('Choose whether to search for Pokemon on basis of "name" or "type":\n').lower()
    while search not in ['name', 'type']:
        search = input('Invalid input. Either input "name" or "type"').lower()

    return search

def poke_input():
    
    name = input('Enter Pokemon name:\n').title()

    print('-'*20)
    return name

def load_data1(name):
    
    df = pd.read_csv('pokedex.csv')

    df.set_index('pokedex_number')

    df = df[['pokedex_number', 'name', 'type_1', 'type_2', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total_points']]

    df = df[df['name'] == name]

    return df

def type_input():
    
    pokegen = input('Enter any desired generation from 1-8 whose Pokemon you wish to explore\n(type "all" if you wish to see all"):\n').title()
    while pokegen not in ['All', '1', '2', '3', '4', '5', '6', '7', '8']:
        pokegen = input('Invalid input. Either input numbers 1-8 or type "all" for all generations').title()
    
    poketype = input('Enter any Pokemon type whose data you wish to explore\n(type "all" if you wish to see all"):\n').title()
    while poketype not in ['All', 'Fire', 'Water', 'Grass', 'Electric', 'Ground', 'Rock', 'Fighting', 'Ice', 'Flying', 'Psychic', 'Ghost', 'Normal', 'Dark', 'Steel', 'Bug', 'Poison', 'Dragon', 'Fairy']:
        poketype = input('Invalid input. Either input any specific Pokémon type or type "all" for all types').title()
    
    print('-'*20)
    return pokegen, poketype


def load_data2(pokegen, poketype):
    
    df = pd.read_csv('pokedex.csv')

    df.set_index('pokedex_number')

    if pokegen != 'All':
        pokegen = int(pokegen)
        df = df[df['generation'] == pokegen]
    
    if poketype != 'All':
        df = df[(df['type_1'] == poketype) | (df['type_2'] == poketype)]

     
    return df


def general_stats(df):

    
    df = df[['pokedex_number', 'name', 'type_1', 'type_2', 'species', 'height_m', 'weight_kg']]

    print('The number of Pokemon based on the filters: {}'.format(str(df.shape[0])))
    print('The general information of these Pokemon:\n')   
    print(df)    


def sort_stats(df):

    df = df[['pokedex_number', 'name', 'hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed', 'total_points']]

    print('')
    print('Top 5 Pokemon with the highest hp stats:\n')  
    print(df.sort_values('hp', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest attack stats:\n')  
    print(df.sort_values('attack', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest defense stats:\n')  
    print(df.sort_values('defense', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest special attack stats:\n')  
    print(df.sort_values('sp_attack', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest special defense stats:\n')  
    print(df.sort_values('sp_defense', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest speed stats:\n')  
    print(df.sort_values('speed', ascending=False).head(5))

    print('')
    print('Top 5 Pokemon with the highest base total stats:\n')  
    print(df.sort_values('total_points', ascending=False).head(5))



def main():
    while True:
        search = first_input()
        if search == 'name':
            name = poke_input()
            df1 = load_data1(name)
            print(df1)
        else:
            pokegen, poketype = type_input()
            df = load_data2(pokegen, poketype)
            general_stats(df)
            sort_stats(df)
        

        restart = input('\nWould you like to restart? Enter yes or no:\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
