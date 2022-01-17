from typing import Dict
import pandas as pd
import json
from pandas.core.frame import DataFrame

FILE = './datos_data_engineer.tsv'
SETTINGS = './settings.json'
SEP = '\t'
ENCODING = 'utf-16le'

def json_settings(json_name: str) -> Dict:
    """[summary]

    Args:
        json_name (str): [description]

    Returns:
        Dict: [description]
    """
    with open(json_name) as settings:
        json_content = json.load(settings)
    return json_content

def read_csv_pandas(filename: str, sep: str=',', encoding: str='utf-8') -> DataFrame:
    """[summary]

    Args:
        filename (str): [description]
        sep (str, optional): [description]. Defaults to ','.
        encoding (str, optional): [description]. Defaults to 'utf-8'.

    Returns:
        DataFrame: [description]
    """
    return pd.read_csv(filename, sep = sep, encoding=encoding)

if __name__ == "__main__":
    df = read_csv_pandas(FILE, SEP, ENCODING)
    count_row = df.shape[0]
    count_columns = df_shape[1]
    data = json_settings(SETTINGS)

    #print(df)

    #print(data)

    # Primer validacion
    if count_columns != len(columns):
        
        raise Exception("El numero de columnas es diferente")

    # Validacion de duplicados
    df.drop_duplicates(inplace=True)
    print("Elimincacion de duplicados")
    print(f"La cantidad de filas del dataframe es: {df.shape[0]}")

    # Validacion de enteros

    # Validacion de nulos

    # Validacion de string

    # Validacion de regex

    # Porcentaje de null por fila

    # Validar porcentaje de dataframe valido

    # Devolver los datos con errores