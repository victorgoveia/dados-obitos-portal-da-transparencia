import requests
import pandas as pd
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor, as_completed


API_URL = "https://transparencia.registrocivil.org.br/api/record/death"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
STATES = [
    "AC",
    "AL",
    "AM",
    "AP",
    "BA",
    "CE",
    "DF",
    "ES",
    "GO",
    "MA",
    "MT",
    "MS",
    "MG",
    "PA",
    "PB",
    "PR",
    "PE",
    "PI",
    "RJ",
    "RN",
    "RO",
    "RR",
    "RS",
    "SC",
    "SP",
    "SE",
    "TO",
]
YEARS = range(2024, 2026)
COLUMNS = ["Ano", "Mês", "Estado", "Cidade", "Quantidade"]


def generate_date_range(year, month):
    start_date = datetime(year, month, 1)
    end_date = (
        (datetime(year, month + 1, 1) - timedelta(days=1))
        if month < 12
        else datetime(year + 1, 1, 1) - timedelta(days=1)
    )
    return start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d")


def fetch_deaths(state, year, month):
    start_date, end_date = generate_date_range(year, month)
    url = f"{API_URL}?start_date={start_date}&end_date={end_date}&state={state}"

    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "data" in data:
            return [
                [year, month, state, item["name"], item["total"]]
                for item in data["data"]
            ]

    except requests.exceptions.RequestException as e:
        print(f"Erro ao buscar dados para {state} ({year}-{month}): {e}")
    return []


def collect_data():
    all_data = []

    with ThreadPoolExecutor(max_workers=10) as executor:
        futures = {
            executor.submit(fetch_deaths, state, year, month): (state, year, month)
            for year in YEARS
            for month in range(1, 13)
            for state in STATES
        }

        for future in as_completed(futures):
            result = future.result()
            if result:
                all_data.extend(result)

    return pd.DataFrame(all_data, columns=COLUMNS)


def save_data(df, output_format="parquet"):
    output_filename = (
        f"dados_obitos_{datetime.now().strftime('%Y%m%d_%H%M%S')}.{output_format}"
    )

    if output_format == "excel":
        df.to_excel(output_filename, index=False)
    elif output_format == "csv":
        df.to_csv(output_filename, index=False, sep=";")
    else:
        df.to_parquet(output_filename, index=False)

    print(f"Dados salvos com sucesso em {output_filename}")


if __name__ == "__main__":
    df = collect_data()
    save_data(df, output_format="parquet")
