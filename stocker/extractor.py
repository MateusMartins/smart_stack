import pandas as pd
import urllib.request

class WebExtractor:

    def get_data_from_url_table(self, url, table_number=0):
        try:
            # GET HTML FROM PAGE
            hdr = {
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
                "Accept-Encoding": "utf-8",
                "Accept-Language": "en-US,en;q=0.8",
                "Connection": "keep-alive",
            }

            req = urllib.request.Request(url, headers=hdr)
            
            try:
                page = urllib.request.urlopen(req)
            except urllib.request as e:
                raise Exception(e.fp.read())

            content = page.read()
            # Get Table from HTML and returns list of all tables on page
            tables = pd.read_html(
                str(content), decimal=",", thousands=".", encoding="utf-8"
            )
        except Exception as e:
            raise Exception(e)

        return tables[table_number]
