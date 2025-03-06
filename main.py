import requests
import json
import pandas as pd
from datetime import datetime, timedelta


def generate_date_range(year, month):
    start_date = datetime(year, month, 1)

    if month == 12:
        end_date = datetime(year + 1, 1, 1) - timedelta(days=1)
    else:
        end_date = datetime(year, month + 1, 1) - timedelta(days=1)
    return start_date, end_date


states = [
    "AC", "AL", "AM", "AP", "BA", "CE", "DF", "ES", "GO", "MA", 
    "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", 
    "RO", "RR", "RS", "SC", "SP", "SE", "TO"
]


columns = ["Ano", "Mês", "Estado", "Cidade", "Quantidade"]
all_data = []


for year in range(2024, 2026):
    for month in range(1, 13):

        start_date, end_date = generate_date_range(year, month)

        start_date_str = start_date.strftime("%Y-%m-%d")
        end_date_str = end_date.strftime("%Y-%m-%d")

        for state in states:

            base_url = f"https://transparencia.registrocivil.org.br/api/record/death?start_date={start_date_str}&end_date={end_date_str}&state={state}"

            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }

            response = requests.get(base_url, headers=headers)

            if response.status_code == 200:
                try:

                    data = response.json()

                    if "data" in data:
                        for item in data["data"]:
                            cidade = item["name"]
                            quantidade = item["total"]

                            all_data.append([year, month, state, cidade, quantidade])

                except json.JSONDecodeError:
                    print("Erro ao decodificar o JSON da resposta.")
            else:
                print(
                    f"Erro na requisição para {state} {start_date_str} a {end_date_str}. Status Code: {response.status_code}"
                )


df = pd.DataFrame(all_data, columns=columns)


output_excel = "dados_obitos_portal_transparencia_2025.xlsx"
df.to_excel(output_excel, index=False)

print(f"Dados salvos com sucesso em {output_excel}")
