import sys
import getpass
import pymysql as mysqldb
import datetime

# userid=input('Username: ')
userid = 'root'
#userpwd = ''  # 비밀번호 입력
userpwd=getpass.getpass('Password: ')
dbname = 'covid'

# connect to MYSQL server
mydb = mysqldb.connect(host='127.0.0.1',
                       user=userid,
                       passwd=userpwd,
                       db=dbname)
cursor = mydb.cursor()

for ldx, line in enumerate(open('Region.csv', 'r')):
    tok = line.strip().split(',')

    if tok[0] == 'code':
        continue

    code = int(tok[0].strip())
    province = tok[1].strip()
    city = tok[2].strip()
    latitude = float(tok[3].strip())
    longitude = float(tok[4].strip())
    elementary_count = int(tok[5].strip())
    kinder_count = int(tok[6].strip())
    university_count = int(tok[7].strip())
    academy_ratio = float(tok[8].strip())
    elderly_popul = float(tok[9].strip())
    elderly_alone = float(tok[10].strip())
    nursing_count = int(tok[11].strip())

    # insert region data into REGION

    sql = """
    INSERT INTO REGION (Region_code,Province,City,Latitude,Longitude,
                       Elementary_school_count,Kindergarten_count,University_count,
                       Academy_ratio,Elderly_population_ratio,Elderly_alone_ratio,Nursing_home_count)
    VALUES(%s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s,%s)
    """
    try:
        cursor.execute(sql, (code, province, city, latitude, longitude, elementary_count,
                             kinder_count, university_count, academy_ratio, elderly_popul,
                             elderly_alone, nursing_count))
        print("Inserting [ %s ] to region" % (code))
    except mysqldb.IntegrityError:
        print("%s already in region" % (code))

mydb.commit()

# close the connection to the database.
cursor.close()
print("Done")
