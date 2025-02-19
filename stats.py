from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
import pandas as pd

#Database credentials
GAME_STATS = "mysql+mysqlconnector://admin:asabasketball@ucd-basketball.cduqug2e0o83.us-east-2.rds.amazonaws.com/game_stats"
#PLAYER_STATS = "mysql+mysqlconnector://admin:asabasketball@ucd-basketball.cduqug2e0o83.us-east-2.rds.amazonaws.com/player_stats"

engine_game_stats = create_engine(GAME_STATS)

#fetch all data from the game_stats table
query_all= "SELECT * FROM game_stats"

df_all = pd.read_sql(query_all, engine_game_stats)

print("What the database looks like: ", df_all)

#Example of how we can extract certain values from the database using SQL
query_fg = "SELECT FG_PCT FROM game_stats"

# Read SQL query into a Pandas DataFrame
df = pd.read_sql(query_fg, engine_game_stats)

# Convert column to list
fg_pct_list = df["FG_PCT"].mean()

#This will give us the average fg percentage for all games
print("Average fg percentage: ", fg_pct_list)

