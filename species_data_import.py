import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


def data_scrape(source):
    response = requests.get(source[1])
    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table")

    data = []
    rows = table.find_all("tr")[1:]
    for row in rows:
        cols = row.find_all("td")
        cols = [col.text.strip() for col in cols]
        data.append(cols)

    df = pd.DataFrame(data, columns=source[2])
    df.to_csv(f'{source[0]}.csv', index=False, header=True, quoting=csv.QUOTE_NONNUMERIC)
    print(f"Data was imported to {source[0]}.csv file")


# List of sources (source format: name, url, columns)
sources = [['list', 'https://komisjafaunistyczna.pl/lista/',
                ['no.', 'latin name', 'polish name', 'category', 'status']],
           ['annex', 'https://komisjafaunistyczna.pl/aneks/',
                ['latin name', 'polish name', 'category', 'status']],
           ['legend', 'https://komisjafaunistyczna.pl/objasnienia/',
                ['category/status', '-', 'description', '', '', '', '', '', '', '', '', '', '', '', '', '']]
           ]

for source in sources:
    data_scrape(source)




