import sys
import getpass
import pymysql as mysqldb
import datetime

#userid=input('Username: ')
userid = 'root'
#userpwd = '' # 비밀번호 입력
userpwd=getpass.getpass('Password: ')
dbname='covid'

# connect to MYSQL server
mydb = mysqldb.connect(host='127.0.0.1',
                       user=userid,
                       passwd=userpwd,
                       db=dbname)
cursor = mydb.cursor()


#TIME_AGE table 에 date, age 먼저 삽입
for ldx, line in enumerate(open('addtional_Timeinfo.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'date':
        continue
   
    if tok[0] == "NULL":
        continue

    confirmed_date = tok[0].strip()   
    confirmed = 0
    decreased = 0

    sql = """
    INSERT INTO TIME_AGE (Date,Age,Confirmed,Decreased)
    VALUES(%s, %s, %s, %s)
    """

    age = {'0s','10s','20s','30s','40s','50s','60s','70s','80s','90s','100s'}

    try:   
        for i in age:
            cursor.execute(sql,(confirmed_date,i,confirmed,decreased))
            print("insert value [ %s ][ %s ] to Timeage" % (confirmed_date,i))
    except mysqldb.IntegrityError:
        print("%s already in Timeage" % (confirmed_date))



#TIME_AGE table 에 confirmed, decreased 값 추가
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL" or tok[2] == "NULL":
        continue

    confirmed_date = tok[10].strip()   
    age = tok[2].strip()
    decreased_date = tok[12].strip()


    try:
        # decreased 값 증가
        if confirmed_date != "NULL":
            sql = "UPDATE TIME_AGE set confirmed = confirmed + 1 where date >= %s and age = %s"
            add = (confirmed_date,age)
            cursor.execute(sql,add)

        # decreased 값 증가
        if decreased_date != "NULL":
            sql = "UPDATE TIME_AGE set decreased = decreased + 1 where date >= %s and age = %s"
            add = (decreased_date,age)
            cursor.execute(sql,add)
        print("add value [ %s ][ %s ] to Timeage" % (confirmed_date,age))
    except mysqldb.IntegrityError:
        print("%s %s already in Timeage" % (confirmed_date,age))
        
        

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
