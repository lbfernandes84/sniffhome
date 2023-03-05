import sys

from sniffhome.app import ConfigurationHandler

import unittest

class TestConfig(unittest.TestCase):
    
    def test_load_label_key_mapper(self):
        map_config = ConfigurationHandler()        
        map_config.load_configuration()
        self.assertEqual(map_config.configMap["price"].label, "Price")

    def test_load_label_key_mapper_2(self):
        map_config = ConfigurationHandler()        
        map_config.load_configuration()
        self.assertEqual(map_config.configMap["real_state_code"].label, "Real State Code")

