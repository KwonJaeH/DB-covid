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


# 해댱 province,city 에서 가장 가까운 병원 위치
position = {}
# 각 병원(Hospital_id) 당 capacity , current
h_capacity= {}

# capacity 설정
sql = "select hospital_id,capacity,current from HOSPITAL"
cursor.execute(sql)

for row in cursor :
    id = row[0]
    capacity = row[1]
    current = row[2]

    h_capacity[id] = (capacity,current)


sql = "select patient_id,province,city from PATIENT_INFO"
cursor.execute(sql)

for row in cursor:

    cur = mydb.cursor()

    id = row[0]
    province = row[1]
    city = row[2]

    if city == 'etc' or city == None:
        city = province

    if city == 'Dalsung-gun':
        city = 'Dalseong-gun'

    sql = "select success from (select EXISTS (select * from REGION where province = '%s' and city='%s') as success)s" % (
    province, city)
    cur.execute(sql)
    success = cur.fetchone()

    if success[0] == 0:
        city = province

    print(province, city)

    # 이미 province, city 해당하는 병원을 구했고 남은 자리가 있다면 continue
    if (province, city) in position:
        h_id = position[(province,city)]
        if h_capacity[h_id][0] > 0 :
            sql = "UPDATE PATIENT_INFO SET Hospital_id = %d where patient_id = %d" % (h_id, id)
            cur.execute(sql)

            capacity = h_capacity[h_id][0] - 1
            current = h_capacity[h_id][1] + 1
            h_capacity[h_id] = [capacity, current]
            
            sql = "UPDATE HOSPITAL SET capacity = %d, current = %d where hospital_id = %d" %(capacity,current,h_id)
            cur.execute(sql)
            continue

    sql = "select latitude, longitude from REGION where province = '%s' and city = '%s'" % (province, city)
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
            if h_capacity[h_id][0] > 0 :
                now_dist = dist
                near_Hid = h_id
    
    position[(province, city)] = near_Hid
    sql = "UPDATE PATIENT_INFO SET Hospital_id = %d where patient_id = %d" % (near_Hid, id)
    cur.execute(sql)

    capacity = h_capacity[near_Hid][0] - 1
    current = h_capacity[near_Hid][1] + 1
    h_capacity[near_Hid] = [capacity, current]
            
    sql = "UPDATE HOSPITAL SET capacity = %d, current = %d where hospital_id = %d" % (capacity,current,near_Hid)
    cur.execute(sql)

    # print(cursor)

mydb.commit()

# close the connection to the database.
cursor.close()
print("Done")
