import os
import json
from openpyxl import load_workbook


TEST_ENVIROMENT = True

CONFIG_DIRECTORY = "../config"
JSON_CONFIG_FILE_NAME = "config.json"
EXCEL_CONFIG_FILE_NAME = "config.xlsx"

class ConfigMap:

    def __init__(self):
        self.key = ""
        self.label = ""
        self.sheet = ""
        self.column = ""

class ConfigurationHandler:

    def __init__(self):
        self.json_obj = None
        self.workbook = None
        self.configMap = dict()
        self.prefix = ""
        if(TEST_ENVIROMENT):
            self.prefix = "TEST_"                

    def load_configuration(self):
        self.__initialize_excel_config()
        self.__load_config_from_json()
        self.__map_labels_to_keys()
        
    def __initialize_excel_config(self):        
        self.workbook = load_workbook(filename=os.path.abspath(os.path.join(CONFIG_DIRECTORY, self.prefix + EXCEL_CONFIG_FILE_NAME)), read_only=True)
    
    def __load_config_from_json(self):
        config_file = open(os.path.abspath(os.path.join(CONFIG_DIRECTORY, self.prefix + JSON_CONFIG_FILE_NAME)))
        self.json_obj = json.load(config_file)
        config_file.close()

    def __map_labels_to_keys(self):
        key_maps = self.json_obj["key_maps"]
        if key_maps:
            for obj_ in key_maps:
                self.configMap[obj_["key"]] = ConfigMap()
                self.configMap[obj_["key"]].key = obj_["key"]
                self.configMap[obj_["key"]].sheet = obj_["sheet"]
                self.configMap[obj_["key"]].column = obj_["column"]
                self.configMap[obj_["key"]].label = self.__get_cell_value(obj_["sheet"], obj_["label_cell"])

    def __get_cell_value(self, sheet, cell):        
        wb_sheet = self.workbook[sheet]                
        return wb_sheet[cell].value
    
    def __load_config_objects(self):
        pass
    

class RealtyAttributeParser:
    def __init__(self):        
        self.realty_code = ""
        self.price = ""
        self.condominium = ""
        self.other_tax = ""
        self.description = ""
        self.neighborhood = ""
        self.street = ""
        self.number = ""
        self.area = ""
        self.rooms = ""
        self.garages = ""

    
class Search:

    def __init__(self):
        self.supplier_code = ""
        self.name = ""
        self.link = ""
        self.use_selenium = False
        self.load_wait_seconds = 0
        self.enable = True
        self.attribute_parser = RealtyAttributeParser()
    
    
