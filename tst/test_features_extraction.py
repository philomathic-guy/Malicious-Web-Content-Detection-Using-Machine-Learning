# This file will test all the functionality of features_extraction.py

import unittest
from features_extraction import *


class TestFeaturesExtraction(unittest.TestCase):
    def test_having_ip_address(self):
        ipv4_address = "172.11.141.23"
        ipv6_address_1 = "fe80:0:0:0:204:61ff:fe9d:f156"
        ipv6_address_2 = "fe80::204:61ff:fe9d:f156"
        ipv6_address_3 = "fe80:0000:0000:0000:0204:61ff:fe9d:f156"
        ipv6_address_4 = "fe80:0:0:0:0204:61ff:254.157.241.86"
        url_1 = "www.google.com"
        url_2 = "888.com"

        # IP address cases
        self.assertEqual(having_ip_address(ipv4_address), -1, "Given input URL has an IP address.")
        self.assertEqual(having_ip_address(ipv6_address_1), -1, "Given input URL has an IP address.")
        self.assertEqual(having_ip_address(ipv6_address_2), -1, "Given input URL has an IP address.")
        self.assertEqual(having_ip_address(ipv6_address_3), -1, "Given input URL has an IP address.")
        self.assertEqual(having_ip_address(ipv6_address_4), -1, "Given input URL has an IP address.")

        # Non IP address cases
        self.assertEqual(having_ip_address(url_1), 1, "Given input URL does not have an IP address.")
        self.assertEqual(having_ip_address(url_2), 1, "Given input URL does not have an IP address.")


if __name__ == "__main__":
    unittest.main()
