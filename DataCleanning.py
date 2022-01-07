####### NULL HANDLING #######
df.isna().sum()
    #muestra los datos nulos de cada columna

df[df.isna().any(1)]
	#trae toda la fila del dato nulo
	
values = {"average_rating" : 4}
android_games.fillna(value=values, inplace=True
	#reemplaza valores null de average_rating por 4
	
for i in range(len(android_games['price'])):
	if android_games['price'][i] != 0:
		android_games['paid'][i] = True
	else:
		android_games['paid'][i] = False
    #valida los valores de la columna paid con la columna Price

####### DUPLICATES #######
# dos filas exactamente iguales
df[df.duplicates()]

# duplicados segun la agrupacion
android_games[android_games.duplicates(subset=['Date', 'rank', 'title', 'total ratings', 'category'], keep=False)]

top_games = android_games.groupby(['Date', 'rank', 'title', 'total ratings', 'installs', 'averages rating',
                                    'growth 30 days', 'growth 60 days', 'price', 'category', 'paid'])['5 star rating', '4 star rating',
                                    '3 star rating', '2 star rating', '1 star rating'].mean()
top_games.reset_index(inplace=True)
top_games[top_games.duplicated(subset='Date', 'rank', 'title', 'total ratings', 'category'), keep=False]

####### UNIFORMIDAD #######
# todos los campos en mayuscula
top_games['category'] = top_games['category'].str.upper()

# muestra todos los valores unicos de esa columna
top_games['category'].unique()

# eliminar categorias que no corresponden
# ~ niega - todos los valores que sean diferentes a FICTION BOOK y BIOGRAPHY BOOK
top_games = top_games[~top_games['category'].isin(['FICTION BOOK', 'BIOGRPHY BOOK'])]


####### DATATYPES #######
# el DS tiene como valores 1M o 1.5K, la funcion saca las letras y multiplica por x cantidad el valor
def installs(x):
    if x[-1] == 'M':
        return(float(x[:-2])*1000000)
    else:
        return(float(x[:-2])*1000)

top_games['installs'] = top_games['installs'].apply(installs)

####### DATATYPES #######
# reemplazar valores
# {Diccionario}
top_games['paid'] = top_games['paid'].replace({True:1, False:0})

####### DATE FORMAT #######
top_games['Date'] = pd.to_datetime(top_games['Date']).dt.strftime('%m/%d/%Y')

####### OUTPUT #######
top_games.to_csv("android_games_limpio.csv")

#Expresiones Regulares
#Librerias fuzzywuzzy y recordlinkage