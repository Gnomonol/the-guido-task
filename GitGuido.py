import requests
import json
from datetime import date
import time
import subprocess


class GitGuido(object):
	""" A class that determines the Github account information of Guido van Rossum. """
	def __init__(self):
		r = requests.get('https://api.github.com/users/gvanrossum')
		self.account_info = json.loads(r.content)

	def get_name(self):
		try:
			self.account_info['name']
		except Exception, e:
			return ("The user has not set their name!")
		else:
			return self.account_info['name']

	def get_username(self):
		return self.account_info['login']

	def get_joined(self):
		return self.account_info['created_at']

	def get_account_age(self):
		get_date = time.strftime("%d/%m/%Y")
		created_date = date(int(self.get_joined()[:4]),int(self.get_joined()[5:7]),int(self.get_joined()[8:10]))
		current_date = date(int(get_date[6:10]), int(get_date[3:5]),int(get_date[:2]))
		return (current_date-created_date).days
		
