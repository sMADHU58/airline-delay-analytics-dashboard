import pandas as pd
import sqlite3
import os

print("Starting data ingestion process...")

# 1. Path to your CSV file
csv_file = "flights.csv"

# Safety check: ensure the file exists
if not os.path.exists(csv_file):
    raise FileNotFoundError(f"Could not find {csv_file} in your project folder!")

# 2. Load a subset of the data (500,000 rows) to keep things fast
# (The full Kaggle dataset has 5+ million rows; 500k is plenty for analysis/modeling)
print("Reading CSV file (this might take 10-15 seconds)...")
df = pd.read_csv(csv_file, nrows=500000, low_memory=False)

# 3. Clean column names (convert to uppercase and replace spaces with underscores)
df.columns = [c.upper().replace(' ', '_') for c in df.columns]

# 4. Connect to SQLite (This automatically creates 'flights.db' in your folder)
print("Connecting to SQLite database...")
conn = sqlite3.connect("flights.db")

# 5. Write the data to a SQL table named 'raw_flights'
print("Writing data to SQL table 'raw_flights'...")
df.to_sql("raw_flights", conn, if_exists="replace", index=False)

# 6. Close the connection
conn.close()

print("Success! 'flights.db' has been created and populated.")