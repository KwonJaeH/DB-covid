import sys
import getpass
import pymysql as mysqldb
import datetime

#userid=input('Username: ')
userid = 'root'
userpwd = 'ehdwogus6277!' # 비밀번호 입력
#userpwd=getpass.getpass('Password: ')
dbname='covid'

# connect to MYSQL server
mydb = mysqldb.connect(host='127.0.0.1',
                       user=userid,
                       passwd=userpwd,
                       db=dbname)
cursor = mydb.cursor()

for ldx, line in enumerate(open('Hospital.csv', 'r', encoding='utf-8-sig')):
    tok=line.strip().split(',')
    
    if tok[0].strip() == 'Hospital_id':
        continue


    id = int(tok[0].strip())
    name = tok[1].strip()
    province = tok[2].strip()
    city = tok[3].strip()
    latitude = float(tok[4].strip())
    longitude = float(tok[5].strip()) 
    capacity = int(tok[6].strip())
    current = int(tok[7].strip())


    # insert region data into REGION

    sql = """
    INSERT INTO HOSPITAL(Hospital_id, Name, Province, City, Latitude, Longitude,
                        Capacity, Current)
    VALUES(%s, %s, %s, %s, %s,%s,%s, %s)
    """
    try:
        cursor.execute(sql,(id,name,province,city,latitude,longitude,capacity,current))
        print("Inserting [ %s ] to Hospital" % (id))
    except mysqldb.IntegrityError:
        print("%s already in Hospital" % (id))

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
