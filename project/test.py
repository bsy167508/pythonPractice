import MySQLdb

<<<<<<< HEAD
db = MySQLdb.connect('localhost','root','12345678','mydb')
db.autocommit(True)
cur = db.cursor()

''
=======
# Open database connection
db = MySQLdb.connect("localhost","root","12345678","mydb" )
# prepare a cursor object using cursor() method
cur = db.cursor() 
db.autocommit(True)

try:
    cur.execute("SELECT VERSION()")
    results = cur.fetchone()
    # Check if anything at all is returned
    if results:
        print results[0]               
except MySQLdb.Error, e:
    print "ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1])

sql="DROP TABLE IF EXISTS customer"
cur.execute(sql)
# Create table as per requirement
sql = """create table customer(
            id int(20) NOT NULL auto_increment,
            name varchar(30),
            is_stud int(2),
            primary key(id) )"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS transactions"
cur.execute(sql)
sql = """create table transactions(
            tid int(20) NOT NULL auto_increment,
            cid int(20) NOT NULL,
            oid int(20) NOT NULL,
            price int NOT NULL,
            primary key(tid) )"""
cur.execute(sql)

cur.execute("DROP TABLE IF EXISTS outlet")
sql = """create table outlet(
            id int(20) NOT NULL auto_increment,
            name varchar(30),
            primary key(id) )"""
cur.execute(sql)

#Populate initial data to database
cur.executemany("insert into outlet(name) values(%s)", ['scoops', 'cafeteria', 'ccd', 'lipton'])
cur.executemany("insert into customer(name, is_stud) values(%s, %s)", [('ram', 1), ('shyam', 0), ('seeta', 1), ('lipton', 0)])
>>>>>>> 20a801d59e6b0b43c4c5c3edd097d99a18bdf288
