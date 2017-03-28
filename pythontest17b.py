import xmlrpclib

server = xmlrpclib.Server('http://www.pythonchallenge.com/pc/phonebook.php')
print server
print server.phone('Leopold')

