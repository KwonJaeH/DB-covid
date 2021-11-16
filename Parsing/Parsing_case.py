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

    if tok[17] == 'NULL':
        continue


    province = tok[4].strip() if tok[4].strip()!="NULL" else None
    infection_case = tok[6] if tok[6] != "NULL" else None

    case_id = int(tok[17].strip())
    city = tok[18].strip() if tok[18].strip()!="NULL" else None
    infection_group = bool(tok[19].strip()) if tok[19].strip()!="NULL" else None
    confirmed = int(tok[20].strip()) if tok[20].strip() != "NULL" else None
    latitude = float(tok[21].strip()) if tok[21].strip()!= "NULL" else None
    longitude = float(tok[22].strip()) if tok[22].strip()!= "NULL" else None
    
    
    if "overseas" in infection_case :
        city = None
        province = None
    

    # insert case data into CASE_INFO

    sql = """
    INSERT INTO CASE_INFO (Case_id,Province,City,Infection_group,Infection_case,Confirmed,
                        Latitude, Longitude)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s)
    """
    try:
        cursor.execute(sql,(case_id,province,city,infection_group,infection_case,confirmed,latitude,longitude))
        print("Inserting [ %s ] to Case" % (case_id))
    except mysqldb.IntegrityError:
        print("%s already in Case" % (case_id))

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
