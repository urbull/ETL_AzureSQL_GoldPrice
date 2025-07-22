import pandas as pd
from sqlalchemy import create_engine
import urllib
from dotenv import load_dotenv
import os


# Dane logowania
load_dotenv()

server = os.getenv("AZURE_SERVER")
database = os.getenv("AZURE_DATABASE")
username = os.getenv("AZURE_USERNAME")
password = os.getenv("AZURE_PASSWORD")

# Polaczenie
params = urllib.parse.quote_plus(
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};DATABASE={database};UID={username};PWD={password}"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# Zaladowanie danych do tabeli: "cena_zlota" w Azure SQL
df = pd.read_csv('gold_prices_clean.csv')
df.to_sql('cena_zlota', engine, if_exists='replace', index=False)

print("Dane załadowane pomyslnie do Azure SQL Database")
