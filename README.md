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
