# Coletor de Dados de Óbitos - Portal da Transparência

Este projeto é um script em Python que acessa a API do Portal da Transparência para coletar dados de óbitos no Brasil. Ele filtra os dados por ano, mês, estado e cidade, e organiza as informações em formatos como Excel, CSV ou Parquet.


## 📌 Funcionalidades
- Acessa a API do Portal da Transparência.
- Filtra os óbitos por mês e ano.
- Coleta dados organizados por estado, cidade, período e quantidade de óbitos.
- Gera arquivos em diferentes formatos: Excel, CSV ou Parquet.
- Utiliza execução paralela para acelerar o processo de coleta de dados.

## 📦 Dependências
Antes de executar o script, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

As principais bibliotecas são:

- requests: Para fazer requisições HTTP à API.
- pandas: Para organizar os dados em DataFrame.
- pyarrow (opcional, para Parquet): Necessário para salvar os dados no formato Parquet.

## 🚀 Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/victorgoveia/dados-obitos-portal-da-transparencia.git
   cd dados-obitos-portal-da-transparencia
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Após a execução, os dados serão salvos em um arquivo no formato escolhido. O formato padrão é Parquet, mas pode-se alterar para Excel ou CSV.

## 📊 Estrutura dos Dados
O arquivo gerado contém as seguintes colunas:
- **Ano**: Ano da ocorrência.
- **Mês**: Mês da ocorrência.
- **Estado**: Estado onde ocorreu o óbito.
- **Cidade**: Cidade onde ocorreu o óbito.
- **Quantidade**: Número de óbitos registrados.

## 📡 Fonte dos Dados
Os dados são coletados diretamente do [Portal da Transparência do Registro Civil](https://transparencia.registrocivil.org.br/).

## ⚠️ Observações
- A API pode sofrer alterações, o que pode impactar a coleta de dados.
- O script pode demorar para executar dependendo do volume de dados coletados.
- O código agora usa execução paralela (threads) para otimizar o processo de coleta.

---

💡 **Contribuições são bem-vindas!** Se encontrar problemas ou quiser sugerir melhorias, abra uma issue ou envie um pull request. 😊

