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
SEP_OUT = '\t'
ENCODING_IN = 'utf-16le'
ENCODING_OUT = 'utf-8'


logging.basicConfig(filename='./loggers.log', format='%(levelname)s - %(asctime)s - %(message)s', level=logging.INFO)


def json_setting(json_name: str) -> Dict:
    """[summary]

    Args:
        json_name (str): [description]

    Returns:
        Dict: [description]
    """
    with open(json_name) as settings:
        json_content = json.load(settings)
    return json_content


def read_csv_pandas(filename: str, sep: str =',', encoding: str='utf-8') -> DataFrame:
    """[summary]

    Args:
        filename (str): [description]
        sep (str, optional): [description]. Defaults to ','.
        encoding (str, optional): [description]. Defaults to 'utf-8'.

    Returns:
        [DataFrame]: [description]
    """
    return pd.read_csv(filename, sep = sep, encoding=encoding)

def write_csv_pandas(dataframe: DataFrame, sep: str=',', encoding: str='utf-8') -> None:
    """[summary]

    Args:
        dataframe (DataFrame): [description]
        sep (str, optional): [description]. Defaults to ','.
        encoding (str, optional): [description]. Defaults to 'utf-8'.
    """
    dataframe.to_csv('final.csv', sep = sep, encoding = encoding, index=False)

if __name__ == "__main__":
    df = read_csv_pandas(FILE,SEP_IN,ENCODING_IN)
    count_row = df.shape[0]
    count_columns = df.shape[1]
    count_nan = int((40*count_columns)/100)
    logging.info(f"La cantidad de filas del dataframe es: {count_row}")
    settings = json_setting(SETTINGS)

    columns = settings['column_list']
    # Primer validacion
    if count_columns != len(columns):
        logging.error("El numero de columnas es diferente", exc_info=True)
        raise Exception("El numero de columnas es diferente")

    # Validacion de duplicados
    df.drop_duplicates(inplace=True)
    logging.info("Eliminacion de duplicados")
    logging.info(f"La cantidad de filas del dataframe es: {df.shape[0]}")

    # Porcentaje de null por fila
    df=df[df.isnull().sum(axis=1)<count_nan]
    logging.info(f"Eliminacion de nan >= {count_nan} por fila")
    logging.info(f"La cantidad de filas del dataframe es: {df.shape[0]}")

    for columna in columns:
        object_column = Columna(settings[columna])
        # Validacion de unicos
        if object_column.unique:
            logging.info(columna)
            df.drop_duplicates(subset=[columna], inplace=True)
            logging.info(f"La cantidad de filas del dataframe despues de las validaciones: {df.shape[0]}")

        # Validacion de tipo
        if object_column.type == 'int':
            # Valida enteros, vacios y nulos
            df = df[~pd.to_numeric(df[columna], errors='coerce').isnull()]
        else: # String
            # Validacion de null
            if object_column.not_null:
                logging.info(columna)
                df.dropna(subset=[columna], inplace=True)
                logging.info(f"La cantidad de filas del dataframe despues de las validaciones: {df.shape[0]}")

            # Validacion de regex
            if object_column.regex:
                df[columna] = df[columna].str.strip()
                df = df[df[columna].str.match(object_column.regex)==True]

    # Validar porcentaje de dataframe valido
    logging.info(f"La cantidad de filas del dataframe original es: {count_row}")
    logging.info(f"La cantidad de filas del dataframe despues de las validaciones: {df.shape[0]}")
    logging.info(f"La cantidad de filas eliminadas: {count_row - df.shape[0]}")
    logging.info(f"La calidad del dataframe es del: {(df.shape[0]/count_row)*100}%")
    
    write_csv_pandas(df, SEP_OUT, ENCODING_OUT)