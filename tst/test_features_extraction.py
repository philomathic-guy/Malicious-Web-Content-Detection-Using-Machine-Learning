# Purpose - This file includes unit tests for all the functionality of features_extraction.py

import unittest
from features_extraction import *
from test import get_prediction_from_url


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

    def test_shortening_services(self):
        url_1 = "bit.ly/akhd9a9"
        url_2 = "http://goo.gl/shan78a"
        url_3 = "https://github.com/philomathic-guy"
        url_4 = "tr.im/adsfaj8"

        # Shortening services links
        self.assertEqual(shortening_service(url_1), -1, "Given input URL is a shortening service URL.")
        self.assertEqual(shortening_service(url_2), -1, "Given input URL is a shortening service URL.")
        self.assertEqual(shortening_service(url_4), -1, "Given input URL is a shortening service URL.")

        # Non-shortening services links
        self.assertEqual(shortening_service(url_3), 1, "Given input URL is a non-shortening service URL.")

    def test_url_length(self):
        # Short URL - Length 41.
        url_1 = "https://docs.python.org/2/library/re.html"
        # Long URL - Length - 73.
        url_2 = "https://github.com/philomathic-guy/Friend-recommendation-using-movie-data"
        # Longer URL - Length 79.
        url_3 = "https://myfunds.000webhostapp.com/new_now/8f66d5a47bf3ec8e6c1ag6s3dc770001a4bd/"

        self.assertEqual(url_length(url_1), 1, "The URL length is not suspicious.")
        self.assertEqual(url_length(url_2), 0, "The URL length is not suspicious.")
        self.assertEqual(url_length(url_3), -1, "The URL length is suspicious.")

    def test_having_at_symbol(self):
        url_1 = "https://docs.python.org/2/library/re.html"
        url_2 = "https://github.com/philomathic-guy/"

        self.assertEqual(having_at_symbol(url_1), 1)
        self.assertEqual(having_at_symbol(url_2), 1)

    def test_full_path(self):
        url_1 = "https://github.com/philomathic-guy/"

        self.assertEqual(get_prediction_from_url(url_1), 1)

    def test_domain_registration_length(self):
        url_1 = "https://github.com/philomathic-guy/"

        hostname_1 = get_hostname_from_url(url_1)
        try:
            domain_1 = whois.query(hostname_1)
            self.assertEqual(domain_registration_length(domain_1))
        except:
            pass

    def test_having_sub_domain(self):
        url_1 = "https://github.com/philomathic-guy/"
        url_2 = "https://www.spit.ac.in"

        self.assertEqual(having_sub_domain(url_1), 1)
        self.assertEqual(having_sub_domain(url_2), 1)


if __name__ == "__main__":
    unittest.main()

