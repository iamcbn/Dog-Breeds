#pip install thefuzz

# Importing the libraries
import pandas as pd
from thefuzz import process

# Reading the CSV file from GitHub
path = r"https://raw.githubusercontent.com/iamcbn/Dog-Breeds/main/Dog%20breed.csv"
df = pd.read_csv(path, header = 0, encoding='latin-1')

# Replace all non-ASCII characters with spaces
df['Breed'] = df['Breed'].str.replace("\xa0", " ")


def breed_search():
    '''
    Purpose: This function searches for different breed of dogs. It is case insensitive.
    Argument: It does not require any arguments.
    Return: It returns a data frame containing information about the searched breed.
    '''
    
    prompt = "Input the breed you are searching for "
    searched_breed = input(prompt)

    
    # Extract fuzzy matches from the 'Breed' column. It returns a list of tuples that contains the match and score. By default, it returns 5 matches (use limit)
    matches = process.extractBests(searched_breed, df['Breed'], score_cutoff = 70) # score_cutoff ensures that it doesn't return anything below the cutoff

    # Extract only the breed names from the matches and stores them in a list
    matched_breeds = [match[0] for match in matches]

    # Create a DataFrame with rows corresponding to the matched breeds
    result_df = df[df['Breed'].isin(matched_breeds)]
    return result_df