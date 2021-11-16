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

    pid = int(tok[0].strip())
    sex = tok[1] if tok[1].strip()!="NULL" else None
    age = tok[2] if tok[2].strip()!="NULL" else None   
    country = tok[3] if tok[3].strip()!="NULL" else None
    province = tok[4] if tok[4].strip()!="NULL" else None
    city = tok[5] if tok[5].strip()!="NULL" else None
    infection_case = tok[6] if tok[6].strip()!="NULL" else None
    infected_by = int(tok[7].strip()) if tok[7].strip()!="NULL" else None
    contact_num = int(tok[8].strip()) if tok[8].strip()!="NULL" else None
    symptom = tok[9] if tok[9].strip()!="NULL" else None
    confirmed_date = tok[10] if tok[10].strip()!="NULL" else None
    released_date = tok[11] if tok[11].strip()!="NULL" else None
    decreased_date = tok[12] if tok[12].strip()!="NULL" else None
    state = tok[13] if tok[13].strip()!="NULL" else None


    # insert oatient data into PATIENT_INFO

    sql = """
    INSERT INTO PATIENT_INFO (Patient_id,Sex,Age,Country,Province,City,Infection_case,Infected_by,
                        Contact_number,Symptom_onset_date,Confirmed_date,Released_date,
                        Decreased_date,State)
    VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s)
    """
    try:
        cursor.execute(sql,(pid,sex,age,province,country,city,infection_case,infected_by,
                            contact_num,symptom,confirmed_date,released_date,decreased_date,state))
        print("Inserting [ %s ] to Patient" % (pid))
    except mysqldb.IntegrityError:
        print("%s already in Patient" % (pid))

mydb.commit()

#close the connection to the database.
cursor.close()
print("Done")
