import pandas as pd

# Wczytanie danych
df = pd.read_csv("gold_prices.csv")

# Walidacja
print("Podstawowe info:")
print(df.info())
print("\nBrakujące wartości:")
print(df.isnull().sum())

# Unikalność daty
if df["date"].is_unique:
    print("\nKażda data jest unikalna")
else:
    print("\nUwaga: są zduplikowane daty")

# Sortowanie i konwersje
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Zapis oczyszczonych danych
df.to_csv("gold_prices_clean.csv", index=False)
print("\nZapisano dane do gold_prices_clean.csv")