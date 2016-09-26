import MySQLdb

db = MySQLdb.connect('localhost','root','12345678','mydb')
db.autocommit(True)
cur = db.cursor()

''