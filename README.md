# Coletor de Dados de Óbitos - Portal da Transparência

Este projeto é um script em Python que acessa a API do Portal da Transparência para coletar dados de óbitos no Brasil. Ele filtra os dados por ano, mês, estado e cidade, organizando-os em um arquivo Excel.

## 📌 Funcionalidades
- Acessa a API do Portal da Transparência.
- Filtra os óbitos por mês e ano.
- Coleta dados organizados por estado e cidade.
- Gera um arquivo Excel contendo os dados coletados.

## 📦 Dependências
Antes de executar o script, instale as dependências listadas no arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

## 🚀 Como Usar
1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o script principal:
   ```bash
   python main.py
   ```
4. Após a execução, os dados serão salvos em um arquivo Excel chamado `dados_obitos_portal_transparencia_2025.xlsx`.

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

---

💡 **Contribuições são bem-vindas!** Se encontrar problemas ou quiser sugerir melhorias, abra uma issue ou envie um pull request. 😊

