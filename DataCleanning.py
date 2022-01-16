"""==================
    NULL HANDLING
====================="""
# show False if its not null and True if its null
df.isnull()

# muestra los datos nulos de cada columna
df.isna().sum()

# ver todo el dataframe y no solo la Serie
df[df.City.isnull()]

# trae toda la fila del dato nulo
df[df.isna().any(1)]

# dropea el registro que tenga nulo
df.dropna(how='any')

# dropea el registro que tenga toda la fila nula
df.dropna(how='all')

# dropea el registro si City o Shape Reported es nulo
df.dropna(subset=['City', 'Shape Reported'], how='any')

# dropea el registro si City y Shape Reported es nulo
df.dropna(subset=['City', 'Shape Reported'], how='any')

# rellenar valores nulos
df['Shape Reported'].value_contents(dropna=False)

# reemplaza valores null de average_rating por 4
values = {"average_rating" : 4}
android_games.fillna(value=values, inplace=True)

# valida los valores de la columna paid con la columna Price
for i in range(len(android_games['price'])):
	if android_games['price'][i] != 0:
		android_games['paid'][i] = True
	else:
		android_games['paid'][i] = False


"""==================
        DUPLICATES
====================="""
# dos filas exactamente iguales
df[df.duplicates()]

# duplicados segun la agrupacion
android_games[android_games.duplicates(subset=['Date', 'rank', 'title', 'total ratings', 'category'], keep=False)]

top_games = android_games.groupby(['Date', 'rank', 'title', 'total ratings', 'installs', 'averages rating',
                                    'growth 30 days', 'growth 60 days', 'price', 'category', 'paid'])['5 star rating', '4 star rating',
                                    '3 star rating', '2 star rating', '1 star rating'].mean()
top_games.reset_index(inplace=True)
top_games[top_games.duplicated(subset='Date', 'rank', 'title', 'total ratings', 'category'), keep=False]

#Expresiones Regulares
#Librerias fuzzywuzzy y recordlinkage

"""==================
    RENAME COLUMNS
====================="""
# list of column names
df.columns

# with dictionary
df.rename(columns = {'Colors Reported':'Colors_Reported', 'Shape Reported':'Shape_Reported'}, inplace=True)

# replace all column names
df_cols = ['city', 'colores reported', 'shape reported', 'state', 'time']
df.columns = df_cols

# while reading the file
#### with list. parametro header sobreescribe el df si ya viene con nombre en columnas
df = pd.read_csv('http://bit.ly/uforeports', names=ufo_colsn header=0)

# replace all the spaces uses _
df.columns = df.columns.str.replace(' ', '_')


"""==================
    REMOVE COLUMNS
====================="""
# drop entire column by name
####  axis=0 its row, axis=1 its column
df.drop('Colors Reported', axis=1, inplace=True)

# drop via list
df.drop(['City', 'State'], axis=1, inplace=True)

# remove rows instead of columns
#### use axis=0
#### 0, 1 its the "name" of the row. Its the index of the row
df.drop([0, 1], axis=0, inplace=True)

# read only specific columns
# by label
df = pd.read_csv('ufo.csv', usecols=['City', 'State'])

# by position
df = pd.read_csv('ufo.csv', usecols=[0, 4])

# by slicing
df = pd.read_csv('ufo.csv', usecols=[: 4])

# drop non-numeric column form a Dataframe
import numpy as np
df.select_dtypes(include=[np.number]).dtypes


"""==================
    SORT DF/SERIES
====================="""
# sort_values is a Series method
movies.title.sort_values()
movies['title'].sort_values()

movies['title'].sort_values(ascending=False)

# sort a dataframe by a Series
movies.sort_values('title')

# sort a dataframe by multiple columns
movies.sort_values(['content_rating', 'duration'])


"""==================
    FILTER ROWS
====================="""
# filter a Dataframe by a Series
# create a list of booleans
booleans[]
for lenght in movies.duration:
    if length >= 200:
        booleans.append(True)
    else:
        booleans.append(False)

# convert to a Series
is_long = pd.Series(booleans)

# compare de Dataframe with Series
movies[is_long]
# the output is all the rows with duration >= 200

# another notation
is_long = movies['duration'] >= 200
movies[is_long]

# true notation
movies[movies.duration >= 200]

# only get the Series.genre of the dataframe with condition
movies[movies.duration >= 200]['genre']

# use loc
#### loc allows you to select rows and columns by label
#### loc[rows_want, columns_want]
movies.loc[movies.duration >= 200, 'genre']

# with function
import random
def CalcularGanancias(retweets):
    ganacia = retweets * random.randint(3, 5)
    return ganancia

df["ganancias"] = df["retweets"].apply(calcularGanancias)

def popularidad(fila):
    resultado = fila["followees"]/fila["followers"]
    return resultado
df["popularidad"] = df.apply(popularidad, axis=1)

"""==================
    MULTIPLE FILTER
====================="""
# & = and, | = or
movies[(movies.duration >= 200) & (movies.genre == 'Drama')]
movies[(movies.duration >= 200) | (movies.genre == 'Drama')]

# multiple values on the same column
movies[movies['genre'].isin(['Crime', 'Drama', 'Action'])]

# eliminar categorias que no corresponden
# ~ niega - todos los valores que sean diferentes a FICTION BOOK y BIOGRAPHY BOOK
top_games = top_games[~top_games['category'].isin(['FICTION BOOK', 'BIOGRPHY BOOK'])]

# muestra todos los valores unicos de esa columna
top_games['category'].unique()


"""==================
    ITERATE DF/SERIES
====================="""
# iterate Series
for c in df.City:
    print(c)

# iterate Dataframe
for index, row in df.iterrows():
    print(index, row.City, row. State)


"""==================
    STRING METHODS
====================="""
#### use "str" to use string methods
# upper a column
df.['item_name'].str.upper()

# filter only the rows who has "Chicken" in the item_name
df[df['item_name']str.contains('Chicken')]

# chain a string method
df.['choice_description'].str.replace('[', '').str.replace(']'. '') 
# with regular expression
df.['choice_description'].str.replace('[\[\]]', '')

"""==================
        DATATYPES
====================="""
# see types
df.dtypes

# int to float
df.['beer_servings'] = df.['beer_servings'].astype(float)

# replace, cast and calculte
df['item_price'].str.replace('$', '').astype(float).mean()

# convert to 0 and 1 
df['item_price'].str.contains('Chicken').astype(int)

# el DS tiene como valores 1M o 1.5K, la funcion saca las letras y multiplica por x cantidad el valor
def installs(x):
    if x[-1] == 'M':
        return(float(x[:-2])*1000000)
    else:
        return(float(x[:-2])*1000)

top_games['installs'] = top_games['installs'].apply(installs)

# reemplazar valores
# {Diccionario}, [Lista]
top_games['paid'] = top_games['paid'].replace({True:1, False:0})

####### DATE FORMAT #######
top_games['Date'] = pd.to_datetime(top_games['Date']).dt.strftime('%m/%d/%Y')


"""==================
        AGRUPATION
            AGG
====================="""
# analize a Series by Category
#### Si responde a la pregunta de "por cada continente" es un groupby
df.groupby('continent')['beer_servings'].mean()

# agg allows you to specify multiple aggregations functions at once
df.groupby('continent')['beer_servings'].agg(['count', 'min', 'max', 'mean'])

"""==================
    EXPLORE A SERIES
====================="""
# get the count, unique, top and freq of a column
movies.genre.describe()

# get a count of each value and how often it appears
movies.genre.value_counts()

# get the percentaje
movies.genre.value_counts(normalize=True)

# unique values
movies.genre.unique()


"""==================
        OUTPUT
====================="""
top_games.to_csv("android_games_limpio.csv")