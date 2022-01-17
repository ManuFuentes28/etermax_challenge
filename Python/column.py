from typing import Dict

class Columna:
    """
        Define la clase columna con sus diferentes configs
    """
    def __init__(self, setting: Dict):
        self.type = setting['type']
        self.unique = setting.get('unique', False)
        self.db_name = setting.get('db_name', '')
        self.not_null = setting.get('not_null', False)
        self.regex = setting.get('regex', '')