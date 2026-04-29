import pandas as pd
import sqlite3

# load data
df = pd.read_csv('data/sample.csv')

# simple cleaning
df.dropna(inplace=True)

# connect to database
conn = sqlite3.connect('database.db')

# store in SQL
df.to_sql('users', conn, if_exists='replace', index=False)

print("Data inserted successfully!")