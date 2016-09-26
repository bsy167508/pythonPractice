import MySQLdb

def curbal(id):
    cur.execute("select balance from customer where id=%s" % id )
    bal = cur.fetchone()
    return bal[0]

def recharge(balance, id):
    cur.execute("update customer set balance=%s+%s where id=%s" % (curbal(id), balance, id))
    
def rechargeAll(balance, id):
    cur.execute("update customer set balance=%s+%s" % (curbal(id), balance))

def purchase(itemprice, cid, oid):
    cur.execute("update customer set balance=%s-%s where id=%s" % (curbal(cid), itemprice, cid))
    cur.execute("insert into transactions(cid, oid, price) values(%s, %s, %s)" % (cid, oid, itemprice))
    
# Open database connection
db = MySQLdb.connect("localhost","root","12345678","mydb" )
db.autocommit(True)
# prepare a cursor object using cursor() method
cur = db.cursor() 

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
            balance int,
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
cur.executemany("insert into customer(name, is_stud, balance) values(%s, %s, %s)", [('ram', 1, 0), ('shyam', 0, 0), ('seeta', 1, 0), ('lipton', 0, 0)])

rechargeAll(1000, 1)
purchase(20, 2, 3)