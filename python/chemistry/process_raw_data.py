import pandas as pd


FILENAME = 'all_data.csv'

chem_df = pd.read_csv(FILENAME, sep='\t', usecols=['Name', 'Smiles'])
chem_df.dropna(inplace=True)
chem_df.to_csv('smiles.csv', index=False, sep='\t')
