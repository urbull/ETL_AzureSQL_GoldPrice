import requests
import pandas as pd
from datetime import datetime, timedelta

#pobieramy z jednego roku, taki limit jest w API NBP
START_DATE = datetime(2024, 7, 15)
END_DATE = datetime.today()
NBP_GOLD_API = "https://api.nbp.pl/api/cenyzlota/{start}/{end}/?format=json"

def fetch_gold_data(start: datetime, end: datetime) -> pd.DataFrame:
    url = NBP_GOLD_API.format(
        start=start.strftime("%Y-%m-%d"),
        end=end.strftime("%Y-%m-%d")
    )
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame(data)
        df.rename(columns={"data": "date", "cena": "price_pln_per_gram"}, inplace=True)
        df["date"] = pd.to_datetime(df["date"])
        return df
    except requests.exceptions.RequestException as e:
        print(f"Błąd pobierania danych: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    df = fetch_gold_data(START_DATE, END_DATE)
    print(df.head())
    df.to_csv("gold_prices.csv", index=False)
    print("Zapisano dane do gold_prices.csv")
