from stocker.extractor import WebExtractor

web_extractor = WebExtractor()
target_url = "https://www.fundamentus.com.br/resultado.php"

# Collect data from any website
fundamentus_table = web_extractor.get_data_from_url_table(
    url=target_url, table_number=0
)

# Rename Columns
fundamentus_table.columns = [
    "Papel",
    "Cotação",
    "P/L",
    "P/VP",
    "PSR",
    "Div.Yield",
    "P/Ativo",
    "P/Cap.Giro",
    "P/EBIT",
    "P/Ativ Circ.Liq",
    "EV/EBIT",
    "EV/EBITDA",
    "Mrg Ebit",
    "Mrg. Líq.",
    "Liq. Corr.",
    "ROIC",
    "ROE",
    "Liq.2meses",
    "Patrim. Líq",
    "Dív.Brut/ Patrim.",
    "Cresc. Rec.5a",
]

dataframe_clean = fundamentus_table.iloc[:, :].copy()
