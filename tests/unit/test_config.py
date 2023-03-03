import sys

from sniffhome.app import ConfigurationHandler

import unittest

class TestConfig(unittest.TestCase):
    
    def test_load_label_key_mapper(self):
        map_config = ConfigurationHandler()        
        self.assertEqual(map_config.key_label_maps["price"], "Price")

    def test_load_label_key_mapper_2(self):
        map_config = ConfigurationHandler()        
        self.assertEqual(map_config.key_label_maps["real_state_code"], "Real State Code")

