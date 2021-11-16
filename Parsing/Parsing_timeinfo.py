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

# TIME_INFO table에 date,test,negative 데이터 삽입

for ldx, line in enumerate(open('addtional_Timeinfo.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'date':
        continue

    if tok[0] == None :
        break

    date = tok[0]
    test = tok[1]
    negative = tok[2]
    confirmed = 0
    released = 0
    decreased = 0
    
    sql = """
    INSERT INTO TIME_INFO (Date,Test,Negative,Confirmed,Released,Decreased)
    VALUES(%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql,(date,test,negative,confirmed,released,decreased))
        print("Inserting [ %s ] to Timeinfo" % (date))
    except mysqldb.IntegrityError:
        print("%s already in Timeinfo" % (date))


# TIME_INFO table에 confirmed,Released,decreased 누적 데이터 삽입
for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue
   
    if tok[10] == "NULL":
        continue

    confirmed_date = tok[10].strip()    
    released_date = tok[11].strip()
    decreased_date = tok[12].strip()

      
    try:
        # confirmed 값 증가
        sql = "UPDATE TIME_INFO set confirmed = confirmed + 1 where date >= %s"
        add = (confirmed_date)
        cursor.execute(sql,add)
      
        # released 값 증가
        if released_date != "NULL":
            sql = "UPDATE TIME_INFO set released = released + 1 where date >= %s"
            add = (released_date)
            cursor.execute(sql,add)

        # decreased 값 증가
        if decreased_date != "NULL":
            sql = "UPDATE TIME_INFO set decreased = decreased + 1 where date >= %s"
            add = (decreased_date)
            cursor.execute(sql,add)
        print("add value [ %s ] [ %s ] [ %s ] to Timeinfo" % (confirmed_date,released_date,decreased_date))
    except mysqldb.IntegrityError:
        print("%s already in Timeinfo" % (confirmed_date))
        
        


mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
