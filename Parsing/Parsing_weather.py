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

for ldx, line in enumerate(open('K_COVID19.csv', 'r')):
    tok=line.strip().split(',')
    
    if tok[0] == 'patient_id':
        continue

    if tok[23] == 'NULL' or tok[10] == 'NULL':
        continue


    province = tok[4].strip() if tok[4].strip()!="NULL" else None
   

    confirmed_date = tok[10]
    avg = float(tok[14]) if tok[14].strip() != "NULL" else None
    min = float(tok[15]) if tok[15].strip() != "NULL" else None
    max = float(tok[16]) if tok[16].strip() != "NULL" else None
    code = int(tok[23].strip())
    # insert weather data into WEATHER

   

    sql = """
    INSERT INTO WEATHER (Region_code,Province,Wdate,Avg_temp,Min_temp,Max_temp)
    VALUES(%s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql,(code,province,confirmed_date,avg,min,max))
        print("Inserting [ %s ] to weather" % (code))
    except mysqldb.IntegrityError:
        print("%s already in weather" % (code))

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
