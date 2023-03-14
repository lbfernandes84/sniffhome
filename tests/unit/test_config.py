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

    def test_get_search_real_state_name_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].real_state_name.parser,'a.publisher__name')

    def test_get_search_real_state_price_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].price.parser,'.price__price-info')
        
    def test_get_search_real_state_condominium_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].condominium.parser,'span.condominium')

    def test_get_search_real_state_other_tax_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].other_tax.parser,'span.iptu')

    def test_get_search_real_state_description_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].description.parser,'h1.title__title')

    def test_get_search_real_state_street_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].street.parser,'p.title__address')

    def test_get_search_real_state_neighborhood_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].neighborhood.parser,'p.title__address')

    def test_get_search_real_state_area_parser(self):                
        self.assertIsNone(self.map_config.searches["VIVAREAL"][0].area.parser)

    def test_get_search_real_state_rooms_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].rooms.parser, "li.features__item--bedroom")

    def test_get_search_real_state_garage_parser(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].garages.parser, "li.features__item--parking")    
    
    def test_get_search_real_state_name_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].real_state_name.extractor_pattern, None)

    def test_get_search_real_state_price_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].price.extractor_pattern,'REGEX<>\d+\.?\d*')
        
    def test_get_search_real_state_condominium_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].condominium.extractor_pattern,'REGEX<>\d+')

    def test_get_search_real_state_other_tax_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].other_tax.extractor_pattern,'REGEX<>\d+')

    def test_get_search_real_state_description_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].description.extractor_pattern, None)

    def test_get_search_real_state_neighborhood_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].neighborhood.extractor_pattern,'SPLIT<>,<>1')
    
    def test_get_search_real_state_street_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].street.extractor_pattern,'SPLIT<>,<>0')

    def test_get_search_real_state_area_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].area.extractor_pattern,'REGEX<>\d+')        

    def test_get_search_real_state_rooms_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].rooms.extractor_pattern, 'REGEX<>\d+')

    def test_get_search_real_state_garage_extractor(self):                
        self.assertEqual(self.map_config.searches["VIVAREAL"][0].garages.extractor_pattern, 'REGEX<>\d+')
