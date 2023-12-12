import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('CompasAnalysis/compas.db')
tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
tables = pd.read_sql_query(tables_query, conn)
dfs = []
for table in tables['name']:
    exec(f'{table} = pd.read_sql_query(f"SELECT * FROM {table}", conn)')
    dfs.append(f'{table}')
conn.close()
print(dfs)
assert len(compas['person_id'].unique()) == 11757
assert len(people) == 11757