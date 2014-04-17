the-guido-task
==============
In this exercise, you'll create a Python class that interacts with a  RESTful API

To start,  please do the following:

 - create a public github account, if you don't already have one
 - fork this repository

The task at hand:
 - create a python class that defines a single class called GitGuido
 - it should have at least the following methods:

         - ``__init__``
           - class constructor that will retrieve the github account
             info
         - get_name
          - returns guido's name
         - get_username
          - returns guido's username
         - get_joined
          - returns the date guido's account was created
         - get_account_age
          - returns (in days) the age of the account

Where do I get the data?
 - using GitHub's API, you will need retrieve the account information for Guido van Rossum (gvanrossum)

  - example using the commandline:

         > curl -i https://api.github.com/users/gvanrossum

          {
            "login": "gvanrossum",
            "name": "Guido van Rossum",
            "created_at": "2012-11-26T18:46:40Z",
          }

 - note: don't freak out if you get a lot more data returned than what we've shown above. the output was truncated to only show the parts that we're interested in

Filelisting
   - run.py
     - imports the GitGuido class and runs its methods
     - we've included this file for you

   - test.py
     - tests for the GitGuido class
       - test that get_name returns a string that is equal to "Guido van Rossum"
       - test that get_username returns a string that is equal to "gvanrossum"
       - come up with 2 more tests using any data regarding Guido's account
         information

   - bonus.py

     !!Bonus Task!!

       - create a commandline script that takes any github username and
         prints out similar account information

         example:

             python bonus.py justinjpacheco

             name: Justin J. Pacheco
             username: justinjpacheco
             joined: 2012-11-26T18:46:40Z
             age: 20 days

Some helpful links:
 - Python datetime: https://docs.python.org/2/library/datetime.html
   - very helpful when doing date calculations
 - Python Requests : http://docs.python-requests.org/en/latest/
   - a great Python HTTP library
 - GitHub API: https://developer.github.com/v3/
