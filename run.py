#!/usr/bin/python

from GitGuido import GitGuido

guido = GitGuido()

print "Guido's name is: {name}".format(name=guido.get_name());
print "Guido's username is: {username}".format(username=guido.get_username());
print "Guido joined on: {joined}".format(joined=guido.get_joined());
print "Guido's account is {days} days old".format(days=guido.get_account_age());
