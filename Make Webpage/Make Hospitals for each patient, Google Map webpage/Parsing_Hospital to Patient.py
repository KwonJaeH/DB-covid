import sys
import getpass
import pymysql as mysqldb
import datetime
import math

# userid=input('Username: ')
userid = 'root'
# userpwd = '' # 비밀번호 입력
userpwd = getpass.getpass('Password: ')
dbname = 'covid'

# connect to MYSQL server
mydb = mysqldb.connect(host='127.0.0.1',
                       user=userid,
                       passwd=userpwd,
                       db=dbname)
cursor = mydb.cursor()

sql = "select patient_id,province,city from PATIENT_INFO"

cursor.execute(sql)

position = {}

for row in cursor:

    cur = mydb.cursor()

    id = row[0]
    province = row[1]
    city = row[2]

    if city == 'etc' or city == None:
        city = province

    if city == 'Dalsung-gun':
        city = 'Dalseong-gun'

    sql = "select success from (select EXISTS (select * from ALL_Region where province = '%s' and city='%s') as success)s" % (
    province, city)
    cur.execute(sql)
    success = cur.fetchone()

    if success[0] == 0:
        city = province

    print(province, city)

    # 이미 province, city 해당하는 병원을 구했으면 continue
    if (province, city) in position:
        sql = "UPDATE PATIENT_INFO SET Hospital_id = %d where patient_id = %d" % (position[(province, city)], id)
        cur.execute(sql)
        continue

    sql = "select latitude, longitude from ALL_Region where province = '%s' and city = '%s'" % (province, city)
    cur.execute(sql)
    result = cur.fetchone()

    now_dist = 100000000  # 임의의 큰 수
    near_Hid = 0
    now_lat = result[0]
    now_long = result[1]

    sql = "select hospital_id,Latitude,Longitude from HOSPITAL"
    cur.execute(sql)

    for a in cur:
        h_id = a[0]
        h_lat = a[1]
        h_long = a[2]

        a = now_lat - h_lat
        b = now_long - h_long
        dist = math.sqrt((a * a) + (b * b))

        if dist < now_dist:
            now_dist = dist
            near_Hid = h_id

    position[(province, city)] = near_Hid
    sql = "UPDATE PATIENT_INFO SET Hospital_id = %d where patient_id = %d" % (near_Hid, id)
    cur.execute(sql)

    # print(cursor)

mydb.commit()

# close the connection to the database.
cursor.close()
print("Done")
