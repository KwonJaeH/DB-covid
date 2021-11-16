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


#TIME_GENDER table 에 date, sex 먼저 삽입
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL" or tok[1] == "NULL":
        continue

    confirmed_date = tok[10].strip()   
    sex = tok[1].strip()
    confirmed = 0
    decreased = 0

    sql = """
    INSERT INTO TIME_GENDER (Date,Sex,Confirmed,Decreased)
    VALUES(%s, %s, %s, %s)
    """

    try:
        cursor.execute(sql,(confirmed_date,sex,confirmed,decreased))
        print("add value [ %s ][ %s ] to Timegender" % (confirmed_date,sex))
    except mysqldb.IntegrityError:
        print("%s %s already in Timegender" % (confirmed_date,sex))



#TIME_GENDER table 에 confirmed, decreased 값 추가
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL" or tok[1] == "NULL":
        continue

    confirmed_date = tok[10].strip()   
    sex = tok[1].strip()
    decreased_date = tok[12].strip()


    try:
        # decreased 값 증가
        if confirmed_date != "NULL":
            sql = "UPDATE TIME_GENDER set confirmed =  confirmed + 1 where date >= %s and sex = %s"
            add = (confirmed_date,sex)
            cursor.execute(sql,add)

        # decreased 값 증가
        if decreased_date != "NULL":
            sql = "UPDATE TIME_GENDER set decreased = decreased + 1 where date >= %s and sex = %s"
            add = (decreased_date,sex)
            cursor.execute(sql,add)
        print("add value [ %s ][ %s ] to Timegender" % (confirmed_date,sex))
    except mysqldb.IntegrityError:
        print("%s %s already in Timegender" % (confirmed_date,sex))
        
        

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
