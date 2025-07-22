#  Pobieranie danych z API NBP o cenie złota, weryfikacja danych i załadowanie ich do Azure SQL (ETL)

## Opis projektu

Ten projekt implementuje ETL korzystając z bazy danych w chmurze Microsoft Azure. Pobiera historyczne dane kursów walut z API Narodowego Banku Polskiego (NBP) z ostatniego roku i przetwarza je za pomocą biblioteki Pandas, a następnie ładuje do bazy danych Azure SQL Database. Końcowo, dane zostały przeanalizowane w Power BI.

## Funkcjonalności

- Pobieranie danych z API NBP  
- Przetwarzanie danych i czyszczenie za pomocą Pandas  
- Ładowanie danych do Azure SQL Database
- Analiza danych w zewnętrznych narzędziach
- Możliwość rozbudowy i łatwej integracji z innymi źródłami danych  

## Technologie

- Python 
- Pandas  
- Azure SQL Database  
- GitHub Actions (CI/CD)  

## Struktura

| Plik/Folder | Opis |
|:------------|:------------|
| .venv/ | Środowisko wirtualne projektu |
| .env | Plik z danymi do połączenia  |
| fetch_gold.py | Pobieranie danych z API NBP |
| transform_gold.py | Sprawdzenie danych |
| upload_to_azure.py | Wysłanie danych do Azure SQL |
| gold_prices.csv | Pobrane dane z API |
| gold_prices_clean.csv | Zweryfikowane dane z API, gotowe do wrzucenia |

## Autor

- Urbull
