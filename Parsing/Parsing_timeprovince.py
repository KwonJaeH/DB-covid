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


#TIME_PROVINCE table 에 date, province 먼저 삽입
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL" or tok[4] == "NULL":
        continue

    confirmed_date = tok[10].strip()   
    province = tok[4].strip()
    confirmed = 0
    released = 0
    decreased = 0

    sql = """
    INSERT INTO TIME_PROVINCE (Date,Province,Confirmed,released,Decreased)
    VALUES(%s, %s, %s, %s, %s)
    """

    try:
        cursor.execute(sql,(confirmed_date,province,confirmed,released,decreased))
        print("insert value [ %s ][ %s ] to Timeprovince" % (confirmed_date,province))
    except mysqldb.IntegrityError:
        print("%s %s already in Timeprovince" % (confirmed_date,province))



#TIME_PROVINCE table 에 confirmed, released, decreased 값 추가
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL" or tok[4] == "NULL":
        continue

    province = tok[4].strip()
    confirmed_date = tok[10].strip()   
    released_date = tok[11].strip()
    decreased_date = tok[12].strip()


    try:
        # confirmed 값 증가
        sql = "UPDATE TIME_PROVINCE set confirmed = confirmed + 1 where date >= %s and province = %s"
        add = (confirmed_date,province)
        cursor.execute(sql,add)
      
        # released 값 증가
        if released_date != "NULL":
            sql = "UPDATE TIME_PROVINCE set released = released + 1 where date >= %s and province = %s"
            add = (released_date,province)
            cursor.execute(sql,add)

        # decreased 값 증가
        if decreased_date != "NULL":
            sql = "UPDATE TIME_PROVINCE set decreased = decreased + 1 where date >= %s and province = %s"
            add = (decreased_date,province)
            cursor.execute(sql,add)
        print("add value [ %s ][ %s ] to Timeprovince" % (confirmed_date,province))
    except mysqldb.IntegrityError:
        print("%s %s already in Timeprovince" % (confirmed_date,province))
        
        

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
