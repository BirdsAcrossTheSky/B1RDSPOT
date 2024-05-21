import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv


# prawdopodbnie optymalniej bylo by rodzielic web scrap z wiki na czesc pobrania danych i transformacji ?
# webscrap zajmuje za duzo czasu
def get_wiki_translation(latin_name):
    url = "https://en.wikipedia.org/wiki/"
    search_url = f"{url}{latin_name.replace(' ', '_')}"
    response = requests.get(search_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        wiki_translation = soup.find('span', {'class': 'mw-page-title-main'}).get_text()

    else:
        print(f'Failed to retrieve the webpage for {latin_name}.')
        return

    return wiki_translation


# Read bird names from CSV file (adjust the filename and column name)
sources = ['list', 'annex']
latin_column = 'latin name'

for source in sources:
    # Initialize an empty list for translations
    english_names = []

    # Read bird names from CSV
    df = pd.read_csv(f'data/imported/{source}.csv')
    latins = df[latin_column]

    # Get English translations
    for latin in latins:
        wiki_result = get_wiki_translation(latin)
        # removing () from wiki names
        if wiki_result is not None:
            wiki_name = wiki_result.split(" (")[0]
        else:
            wiki_name = wiki_result

        english_names.append(wiki_name)

    df['english name'] = english_names
    col_order = ['latin name', 'polish name', 'english name', 'category', 'status']
    df = df[col_order]

    # Datafix 1
    if source == 'list':
        row_index = df[df['latin name'] == 'Columba livia forma urbana'].index
        df.loc[row_index, 'english name'] = 'Feral pigeon'

    # Datafix 2
    if source == 'annex':
        row_index = df[df['latin name'] == 'Coracias caudataus'].index
        df.loc[row_index, 'english name'] = 'Lilac-breasted roller'

    # Save translations to a new CSV file
    df.to_csv(f'data/to_db/{source}_db.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)  # column position will be adjusted in database
    print(f'Translations saved to {source}_db.csv.')

