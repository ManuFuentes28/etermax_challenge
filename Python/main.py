from asyncore import write
from typing import Dict
import pandas as pd
import json
import logging
import re
from pandas.core.frame import DataFrame
from column import Columna

FILE = './datos_data_engineer.tsv'
SETTINGS = './settings.json'
SEP_IN = '\t'
SEP_OUT = '|'
ENCODING_IN = 'utf-16le'
ENCODING_OUT = 'uft-8'

logging.basicConfig(filename='./loggers.log', format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)

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
    return pd.read_csv(filename, sep=sep, encoding=encoding)

def write_csv_pandas(dataframe: DataFrame, sep: str=',', encoding: str='uft-8') -> None:
    """[summary]

    Args:
        dataframe (DataFrame): [description]
        sep (str, optional): [description]. Defaults to ','.
        encoding (str, optional): [description]. Defaults to 'uft-8'.

    Raises:
        Exception: [description]
    """
    dataframe.to_csv('final.csv', sep=SEP_OUT, encoding=ENCODING_OUT)

if __name__ == "__main__":
    df = read_csv_pandas(FILE, SEP_IN, ENCODING_IN)
    count_row = df.shape[0]
    count_columns = df_shape[1]
    count_nan = int((40*count_columns)/100) # porcentaje de para nulos 
    logging.info(f"La cantidad de filas del dataframe es: {count_row}")
    settings = json_settings(SETTINGS)
    
    columns = settings['column_list']
    
    # Primer validacion
    df.drop_duplicates(inplace=True)
    logging.info("------- Eliminacion de duplicados -------")
    logging.info(f"La cantidad de filas del dataframe es: {df.shape[0]}")
    
    # Porcentaje de null por fila
    df = df[df.isnull().sum(axis=1)<count_nan]
    logging.info(f"Eliminacion de NaN >= {count_nan} por fila")
    logging.info(f"La cantidad de filas del dataframe es: {df.shape[0]}")

    for columna in columns:
        objetc_column = Columna(settings[columna])
        
        # Validacion de unicos
        if objetc_column.unique:
            df.drop_duplicates(subset=[columna], inplace=True)
            logging.info(f"La cantidad de filas del dataframe despues de las validaciones es: {df.shape[0]}")
        
        # Validacion de tipo de dato
        if objetc_column.type == 'int':
            # Valida enteros, vacíos y nulos
            df = df[~pd.to_numeric(df[columna], errors='coerce').isnull()]
        else: # String
            # Validación de null
            if objetc_column.not_null:
                df.dropna(subset=[columna], inplace=True)
                logging.info(f"La cantidad de filas del dataframe despues de las validaciones es: {df.shape[0]}")
                
            # Validacion de regex
            if objetc_column.regex:
                df[columna] = df[columna].str.strip() # Elimina espacios
                df = df[df[columna].str.match(objetc_column.regex)==True]
    
    # Validar porcentaje de dataframe valido
    logging.info(f"La cantidad de filas del dataframe original es: {count_row}")
    logging.info(f"La cantidad de filas del dataframe despues de las validaciones es: {df.shape[0]}")
    logging.info(f"Cantidad de filas eliminadas: {count_row - df.shape[0]}")
    logging.info(f"La calidad del dataframe es del: {(df.shape[0]/count_row)*100}%")