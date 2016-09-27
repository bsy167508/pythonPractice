import MySQLdb, random

# Open database connection
db = MySQLdb.connect("localhost","root","12345678","mydb" )
db.autocommit(True)
# prepare a cursor object using cursor() method
cur = db.cursor() 
# see if connection was made successfully.
try:
    cur.execute("SELECT VERSION()")
    results = cur.fetchone()
    # Check if anything at all is returned
    if results:
        print "Connected to database."               
except MySQLdb.Error as e:
    print "ERROR %d IN CONNECTION: %s" % (e.args[0], e.args[1])
 
 
 # Create tables as per requirement   
sql="DROP TABLE IF EXISTS student"
cur.execute(sql)

sql = """create table student(
            stu_id int NOT NULL auto_increment,
            name varchar(30),
            gender ENUM('male', 'female'),
            primary key(stu_id) )"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS course"
cur.execute(sql)
sql = """create table course(
            course_id int NOT NULL auto_increment,
            course_name varchar(30),
            instructor varchar(30),
            primary key(course_id) )"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS enroll"
cur.execute(sql)
sql = """create table enroll(
            stu_id int NOT NULL,
            course_id int NOT NULL)"""
            
cur.execute(sql)

sql="DROP TABLE IF EXISTS grades"
cur.execute(sql)
sql = """create table grades(
            id int NOT NULL auto_increment,
            stu_id int NOT NULL,
            course_id int NOT NULL,
            grade varchar(12),
            primary key(id) )"""
            
cur.execute(sql)

#Populate the tables with suitable data.
cur.executemany("insert into student(name, gender) values(%s, %s)", [('abhishek', 1), ('karan', 1), ('priyanka', 2), ('monika', 2), ('ram', 1), ('shyam', 1), ('seeta', 2), ('geeta', 2)])
cur.executemany("insert into course(course_name, instructor) values(%s, %s)", [('Signal Theory', 'Mahim Sagar'), ('Telecom Software Lab', 'Subrat Kar'), ('Computer Networks', 'Ranjan Bose'), ('Broadband Communication', 'Mahim Sagar'), ('Coding Theory', 'Ranjan Bose'), ('Digital Communication', 'Shankar Prakriya'), ('Telecom Technology', 'Subrat Kar'), ('Telecom Management Systems', 'Shankar Prakriya')])

#enroll students
for i in range(1,9):
    if not i%2==0:
        cur.executemany("insert into enroll(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(1,5)])
    else:
        cur.executemany("insert into enroll(stu_id, course_id) values(%s, %s)", [(i, k) for k in range(5,9)])

#grade the students
gradeMarks = ['a', 'a-','b', 'b-', 'c', 'c-', 'd', 'e', 'f'][::-1]
for i in range(1,9):
    if not i%2==0:
        c = random.randint(0,8)
        cur.executemany("insert into grades(stu_id, course_id, grade) values(%s, %s, %s)", [(i, k, gradeMarks[c]) for k in range(1,5)])
    else:
        c = random.randint(0,8)
        cur.executemany("insert into grades(stu_id, course_id, grade) values(%s, %s, %s)", [(i, k, gradeMarks[c]) for k in range(5,9)])
        
 #Find students enrolled in both CTheory and TMS       
 
sql = "select distinct s.name from student as s join course as c join enroll as e on e.course_id=c.course_id and e.stu_id=s.stu_id where course_name='Coding Theory' or course_name='Telecom Management Systems'"
cur.execute(sql)
result = cur.fetchall()
print "Subject takers"
for r in result:
    print r[0]

print "\nA scorers"
#Print names of students who scored atleast an A in any subjects taught by Subrat Kar
sql = "select distinct s.name from student as s join grades as g join enroll as e join course as c on e.course_id=c.course_id and s.stu_id=g.stu_id and s.stu_id=e.stu_id where c.instructor='Subrat Kar' and g.grade='a'"
cur.execute(sql)
result = cur.fetchall()

for r in result:
    print r[0]
 
#Avg score for each course
print "\nEnter respective course_id to get average marks"
cid = raw_input()
sql="select grade from grades where course_id=%s" % cid
cur.execute(sql)
result = cur.fetchall()
#create marks list
marks = []
for r in result:
    marks=marks+[gradeMarks.index(r[0])+2]
print reduce(lambda x, y: x + y, marks) / float(len(marks))

#girl student who topped in the course
print "\nEnter respective course_id"
cid = raw_input()
sql="select s.name, g.grade from grades as g join student as s on s.stu_id=g.stu_id where g.course_id=%s and s.gender=2" % cid
cur.execute(sql)
result = cur.fetchall()
lname=[]
lmarks=[]
for r in result:
    lname.append(r[0])
    lmarks.append(r[1])

for i in range(len(lmarks)):
    lmarks[i]=gradeMarks.index(lmarks[i])+2

sql="select g.grade from grades as g join student as s on s.stu_id=g.stu_id where g.course_id=%s" % cid
cur.execute(sql)
result = cur.fetchall()
lmarks2=[]
for r in result:
    lmarks2.append(r[0])

for i in range(len(lmarks)):
    lmarks2[i]=gradeMarks.index(lmarks2[i])+2
    
if max(lmarks)>max(lmarks2):
    indices = [index for index, val in enumerate(lmarks) if val == max(lmarks)]
    for i in indices:
        print lname[lmarks.index(i)]
else:
    print "No girl topper"