import unittest
from datetime import date
import time
import subprocess
import requests
from GitGuido import GitGuido

class TestGuido(unittest.TestCase):

	def setUp(self):
		self.Guido = GitGuido()

	def test_0_get_name(self):
		self.assertEqual(self.Guido.get_name(), "Guido van Rossum")

	def test_1_get_username(self):
		self.assertEqual(self.Guido.get_username(), "gvanrossum")

	def test_2_get_joined(self):
		self.assertEqual(self.Guido.get_joined(), "2012-11-26T18:46:40Z")

	def test_3_get_account_age(self):
		get_date = time.strftime("%d/%m/%Y")
		current_date = date(int(get_date[6:10]), int(get_date[3:5]),int(get_date[:2]))
		self.assertEqual(self.Guido.get_account_age(), (current_date - date(2012, 11, 26)).days)

	def tearDown(self):
		self.Guido = None

if __name__ == '__main__':
    unittest.main()
