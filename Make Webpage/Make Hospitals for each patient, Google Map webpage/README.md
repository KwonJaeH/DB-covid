
Hospital.csv 파일과 추가 Region.csv 파일을 읽어,  
MYSQL table에 삽입 후,  
Patient table에 "hospital_id" attribute를 추가하여 해당 환자가 어디 병원에 입원 중인지 나타냄.    

Hospital id 를 입력하면 해당 병원에 입원해있는 환자 수와 환자 출력.  
환자 정보에서 Hospital_id를 클릭하면 병원 위치를 Google Map 을 이용하여 출력.    

Hospital.csv file  
Hospital_id, Hospital_name, province, city , latitude, longitude, capacity(총 수용 인원), current(현재 수용 인원) 이 저장되어있음.  
Region.csv file  
각 province, city 에 해당하는 latitude, longitude 가 저장되어있음.  

------------------------------------------------------------------------------------
**단계별 구분**
- Hospital.csv, Region.csv 파일을 읽어와 MYSQL 데이터베이스에 저장  
- Region 에서 환자의 주소에 해당하는 latitude, longitude와 병원의 latitude, longitude를 거리 계산하여 가장 가까운 곳에 병원 배치.  
  capacity가 가득 찼으면 그 다음으로 가까운 병원 배치.  
- Hospital_id 를 입력하면 해당 병원에 입원해있는 환자 수와 환자 출력 및 환자 정보에서 Hospital_id 클릭 시, 병원의 Google Map 출력  

