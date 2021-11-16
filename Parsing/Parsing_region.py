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

    if tok[23] == 'NULL':
        continue


    province = tok[4].strip() if tok[4].strip()!="NULL" else None
    city = tok[5].strip() if tok[5].strip()!="NULL" else None
    
    infection_case = tok[6] if tok[6] != "NULL" else None

    code = int(tok[23].strip())
    latitude = float(tok[24].strip()) if tok[24].strip()!= "NULL" else None
    longitude = float(tok[25].strip()) if tok[25].strip()!= "NULL" else None
    elementary_count = int(tok[26].strip()) if tok[26].strip() !="NULL" else None
    kinder_count = int(tok[27].strip()) if tok[27].strip() !="NULL" else None
    university_count = int(tok[28].strip()) if tok[28].strip() !="NULL" else None
    academy_ratio = float(tok[29].strip()) if tok[29].strip() !="NULL" else None
    elderly_popul = float(tok[30].strip()) if tok[30].strip() !="NULL" else None
    elderly_alone = float(tok[31].strip()) if tok[31].strip() !="NULL" else None
    nursing_count = int(tok[32].strip()) if tok[32].strip() !="NULL" else None
 
    # insert region data into REGION

    sql = """
    INSERT INTO REGION (Region_code,Province,City,Latitude,Longitude,
                       Elementary_school_count,Kindergarten_count,University_count,
                       Academy_ratio,Elderly_population_ratio,Elderly_alone_ratio,Nursing_home_count)
    VALUES(%s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s)
    """
    try:
        cursor.execute(sql,(code,province,city,latitude,longitude,elementary_count,
                            kinder_count,university_count, academy_ratio,elderly_popul,
                            elderly_alone,nursing_count))
        print("Inserting [ %s ] to region" % (code))
    except mysqldb.IntegrityError:
        print("%s already in region" % (code))

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
