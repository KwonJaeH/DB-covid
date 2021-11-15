
2021.11.15 

covid.csv 파일 읽은 후, mysql 데이터베이스에 데이터 삽입. yeah

예외 처리 ----------------

CASE 데이터 삽입
 : case_id 가 "NULL" 일 경우 continue 사용, case_id = "NULL" 인 경우 데이터를 삽입하지 않음.
   "overseas" in infection_case 인 경우(해외 유입 케이스), 시/구/동 정보가 없어도 되므로
   city, province 에 None 삽입해 데이터베이스에 NULL 삽입.
   나머지 컬럼들은 "NULL" 일 경우 None을 삽입해 데이터베이스에 NULL 삽입.
  
 
PATIENT 데이터 삽입
 : patient_id 는 "NULL" 인 경우가 없으므로 int 형 변환 후 삽입.
   나머지 컬럼들은 "NULL" 일 경우 None을 삽입해 데이터베이스에 NULL을 삽입.


REGION 데이터 삽입
 : region_code 가 "NULL" 일 경우 continue 사용, region_code = "NULL" 인 경우 데이터를 삽입하지 않음.
   나머지 컬럼들은 "NULL" 일 경우 None을 삽입해 데이터베이스에 NULL을 삽입.


WEATHER 데이터 삽입
 : region_code 를 같이 사용하기 때문에 마찬가지로,
   region_code 가 "NULL" 일 경우 continue 사용, region_code = "NULL" 인 경우 데이터를 삽입하지 않음.
   region_code 와 date 가 복합키로 사용되므로, region_code 가 중복되더라도 삽입.
   나머지 컬럼들은 "NULL" 일 경우 None을 삽입해 데이터베이스에 NULL을 삽입.
 
-------------------------------------------------------------------------------------------------------------------------------------------------
