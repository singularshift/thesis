# First, I want to load all csv files from the csvfileselection folder
# Then, I want to assign the correct label to each row based on the filename
# Then, I want to calculate the trading probabilities of each row based on the filename (buyerPaid/sharesBought)
# Then, I want to save all results in a new csv file

import os
import pandas as pd

# Load all csv files from the csvfileselection folder
csv_files = [f for f in os.listdir('csvfileselection') if f.endswith('.csv')]

# Create an empty list to store all dataframes
all_dfs = []

# Process each csv file
for file in csv_files:
    # Read the CSV file
    df = pd.read_csv(f'csvfileselection/{file}')
    
    # Get the query ID (last part before .csv)
    query_id = file.split('_')[-1].replace('.csv', '')
    
    # Add the label column
    df['label'] = query_id
    
    # Calculate probabilities
    df['probabilities'] = df['buyerPaid'] / df['sharesBought']
    
    # Append to our list of dataframes
    all_dfs.append(df)

# Combine all dataframes into one
master_df = pd.concat(all_dfs, ignore_index=True)

# Save the combined dataframe to a new CSV file
master_df.to_csv('csvfileselection/electionmaster.csv', index=False)

print("Master CSV file has been created successfully!")





