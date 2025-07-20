import pandas as pd
import csv


csv_filename = 'legend.csv'
legend_df = pd.read_csv(f'data/imported/{csv_filename}')

# use only columns with information
cols_to_use = [0, 2]
legend_df = legend_df.iloc[:, cols_to_use]

# delete empty rows and divide into two datasets
empty_row_index = legend_df.index[legend_df.isnull().all(axis=1)].tolist()[0]
category_df = legend_df.loc[:empty_row_index - 1].copy()
status_df = legend_df.loc[empty_row_index + 1:].copy()

# drop empty values for nulls in db
category_df.dropna(inplace=True)
status_df.dropna(inplace=True)

# separate column names
category_column = category_df.columns[0].split('/')[0]
status_column = status_df.columns[0].split('/')[1]
category_df.rename(columns={category_df.columns[0]: category_column}, inplace=True)
status_df.rename(columns={status_df.columns[0]: status_column}, inplace=True)

# Save to csv
category_df.to_csv('data/to_db/category_db.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)
status_df.to_csv('data/to_db/status_db.csv', index=False, quoting=csv.QUOTE_NONNUMERIC)


