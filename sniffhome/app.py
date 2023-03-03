import os
import json
from openpyxl import load_workbook


TEST_ENVIROMENT = True

CONFIG_DIRECTORY = "../config"
JSON_CONFIG_FILE_NAME = "config.json"
EXCEL_CONFIG_FILE_NAME = "config.xlsx"

class ConfigurationHandler:

    def __init__(self):
        self.json_obj = None
        self.workbook = None
        self.key_label_maps = dict()
        self.prefix = ""
        if(TEST_ENVIROMENT):
            self.prefix = "TEST_"        
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
                self.key_label_maps[obj_["key"]] = self.__get_cell_value(obj_["cell"])

    def __get_cell_value(self, sheet_cell):
        sheet_cell_components = sheet_cell.split(":")
        sheet_name = sheet_cell_components[0].strip()
        cell_value = sheet_cell_components[1].strip()
        sheet = self.workbook[sheet_name]                
        return sheet[cell_value].value
    
