import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# 1. Pobieranie danych

# df = pd.read_csv('dane_csv.csv', delimiter=None, header='infer', index_col=None, usecols=None, dtype=None, engine=None, converters=None, true_values=None, false_values=None, skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None, keep_default_na=True, na_filter=True, skip_blank_lines=True, parse_dates=None, date_format=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None, compression='infer', thousands=None, decimal='.', lineterminator=None, quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None, encoding=None, encoding_errors='strict', dialect=None, on_bad_lines='error', low_memory=True, memory_map=False, float_precision=None, storage_options=None)

url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-03-31/beers.csv"

try:
    df = pd.read_csv(url)
    print('dane pobrane')
except Exception as e:
    print(f'Błąd {e}')
    print('Używam danych zapasowych')
    data = {
        'nazwa': ['IPA','IPA', 'Lager', 'Stout', 'Pilsner', 'Wheat', 'Porter', 'Ale', 'Bock'],
        'alkohol': [6.5, 6.5, 5.0, 7.2, 4.8, 5.2, 5.8, 5.5, 6.8],
        'goryczka': [65, 65, np.nan, 45, 30, 15, 40, 35, 25],
        'ocena': [4.2, 4.2, 3.8, 4.5, 3.9, 3.7, 4.1, 4.0, 4.3],
        'styl': ['IPA', 'IPA', 'Lager', 'Ciemne', 'Lager', np.nan, 'Ciemne', 'Jasne', 'Ciemne']
    }
    df = pd.DataFrame(data)

print(df)

# 2. Podstawowe informacje
print('\n' + '='*50)
print('PODSTAWOWE INFORMACJE')
print('='*50)

print(f'Wymiary danych: {df.shape}')
print(f'Liczba wierszy: {df.shape[0]}')
print(f'Liczba kolumn: {df.shape[1]}')

# 3. Podglad danych
print('\n' + '='*50)
print('PODGLĄD DANYCH')
print('='*50)

print('Pierwsze 5 piw:')
print(df.head())
print('5 ostatnich piw')
print(df.tail())

# 4. Typy danych
print('\n' + '='*50)
print('TYPY DANYCH')
print('='*50)

print(f'\n{df.info()}')

# 5. Statystyki numeryczne
print('\n' + '='*50)
print('STATYSTYKI NUMERYCZNE')
print('='*50)

kolumny_numeryczne = df.select_dtypes(include='number').columns
if len(kolumny_numeryczne) > 0:
    print('Statystyki dla cech numerycznych:')
    print(df[kolumny_numeryczne].describe())
else:
    print('Brak kolumn numerycznych w danych')

# 6. Statystyki kategoryczne
print("\n" + "="*50)
print("STATYSTYKI KATEGORYCZNE")
print("="*50)

kolumny_tekstowe = df.select_dtypes(include='object').columns
if len (kolumny_tekstowe) > 0:
    for kolumna in kolumny_tekstowe:
        print(f'\nKolumna: {kolumna}')
        print(f'Unikalnych wartości: {df[kolumna].unique()}')
        print(f'Liczba unikalnych wartości: {len(df[kolumna].unique())}')
        print('3 jajczęstrze wartości:')
        print(df[kolumna].value_counts().head(3))
    else:
        print('Brak kolumn kategorycznych w danych')

# 7. Brakujące wartości
print("\n" + "="*50)
print("BRAKUJĄCE WARTOŚCI")
print("="*50)

brakujace = df.isna().sum()  #  liczba braków w kolumnach
if brakujace.sum() > 0:
    print('Kolumny z brakującymi wartościami:')
    for kolumna in df.columns:
        if df[kolumna].isna().sum() > 0:
            braki_liczbowo = df[kolumna].isnull().sum()
            braki_procentowo = (braki_liczbowo / len(df)) * 100
            print(f'    {kolumna}: {braki_liczbowo} ({braki_procentowo:.2f}%)')

# 8. Wizualizacje

print("\n" + "=" * 50)
print("TWORZENIE WYKRESÓW")
print("=" * 50)




