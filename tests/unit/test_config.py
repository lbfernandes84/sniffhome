import os
import sys

from sniffhome.app import ConfigurationHandler
from sniffhome import settings

import unittest

class TestConfig(unittest.TestCase):
    
    def setUp(self):
        settings.ENVIROMENT = "TEST"
        settings.CONFIG_DIRECTORY = os.path.abspath("./files")
        self.map_config = ConfigurationHandler()        
        self.map_config.load_configuration()
    
    def test_load_label_key_mapper(self):        
        self.assertEqual(self.map_config.config_map["price"].label, "Price")

    def test_load_label_key_mapper_2(self):        
        self.assertEqual(self.map_config.config_map["real_state_code"].label, "Real State Code")

    def test_get_supplier_code_right(self):        
        self.assertIn("VIVAREAL",self.map_config.searches)

    def test_get_supplier_search_one_value(self):        
        self.assertEqual(len(self.map_config.searches["VIVAREAL"]), 1)

    def test_get_search_name_read(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].name, "Casa Nova Lima")        

    def test_get_search_use_selenium(self):                
        self.assertFalse(self.map_config.searches["VIVAREAL"][0].use_selenium)

    def test_get_search_wait_seconds(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].load_wait_seconds, 10)

    def test_get_search_is_enable(self):                
        self.assertTrue(self.map_config.searches["VIVAREAL"][0].enable)

    def test_get_search_realty_container(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].container_parser,"section.results__main a")

    def test_get_search_change_page(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].change_page_parser,'test[change="get"]')
        
        

