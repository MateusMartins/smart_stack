from stocker.extractor import WebExtractor

web_extractor = WebExtractor()
target_url = "https://www.fundsexplorer.com.br/ranking"

# Collect data from any website
content_table = web_extractor.get_data_from_url_table(url=target_url, table_number=0)

# Rename Columns
schema_columns = [
    "CODIGO_DO_FUNDO",
    "SETOR",
    "PRECO_ATUAL",
    "LIQUIDEZ_DIARIA",
    "DIVIDENDO",
    "DIVIDEND_YIELD",
    "DY_3M_ACUMULADO",
    "DY_6M_ACUMULADO",
    "DY_12M_ACUMULADO",
    "DY_3M_MEDIA",
    "DY_6M_MEDIA",
    "DY_12M_MEDIA",
    "DY_ANO",
    "VARIACAO_PRECO",
    "RENTAB_PERIODO",
    "RENTAB_ACUMULADA",
    "PATRIMÔNIO_LIQ",
    "VPA",
    "P/VPA",
    "DY_PATRIMONIAL",
    "VARIACAO_PATRIMONIAL",
    "RENTAB_PATR_NO_PERIODO",
    "RENTAB_PATRACUMULADA",
    "VACANCIA_FISICA",
    "VACANCIA_FINANCEIRA",
    "QUANTIDADE_ATIVOS",
]

content_table.columns = schema_columns
