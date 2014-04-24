import requests
from datetime import date
import time
import subprocess
import sys
username = sys.argv[1]

class GitGuido(object):
	""" A class that determines the Github account information of any user. """
	def __init__(self):
		r = requests.get('https://api.github.com/users/{}'.format(username))
		self.account_info = r.content

	def get_name(self):
		""" Users on Github are defaulted to no name, so the exception is to defend against that. """
		try:
			idx1 = self.account_info.index('"name":"')
		except Exception, e:
			return ("The user has not set their name!")
		else:
			idx1 = self.account_info.index('"name":"')
			idx2 = self.account_info[idx1:].index('",')
			return self.account_info[idx1 + len('"name":"'): idx1 + idx2]

	def get_username(self):
		idx1 = self.account_info.index('"login":"')
		idx2 = self.account_info[idx1:].index('",')
		return self.account_info[idx1 + len('"login":"'): idx1 + idx2]

	def get_joined(self):
		idx1 = self.account_info.index('"created_at":"')
		idx2 = self.account_info[idx1:].index('",')
		return self.account_info[idx1 + len('"created_at":"'): idx1 + idx2]

	def get_account_age(self):
		get_date = time.strftime("%d/%m/%Y")
		created_date = date(int(self.get_joined()[:4]),int(self.get_joined()[5:7]),int(self.get_joined()[8:10]))
		current_date = date(int(get_date[6:10]), int(get_date[3:5]),int(get_date[:2]))
		return (current_date-created_date).days

if __name__ == '__main__':
	user = GitGuido()
	print("name: {name}".format(name=user.get_name()))
	print("username: {username}".format(username=user.get_username()))
	print("joined: {joined}".format(joined=user.get_joined()))
	print("age: {days} days".format(days=user.get_account_age()))
