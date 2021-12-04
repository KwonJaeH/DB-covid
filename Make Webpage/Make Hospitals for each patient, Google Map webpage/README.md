
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
[1] Hospital.csv, Region.csv 파일을 읽어와 MYSQL 데이터베이스에 저장  
[2] Region 에서 환자의 주소에 해당하는 latitude, longitude와 병원의 latitude, longitude를 거리 계산하여 가장 가까운 곳에 병원 배치.  
    capacity가 가득 찼으면 그 다음으로 가까운 병원 배치.  
[3] Hospital_id 를 입력하면 해당 병원에 입원해있는 환자 수와 환자 출력 및 환자 정보에서 Hospital_id 클릭 시, 병원의 Google Map 출력 

------------------------------------------------------------------------------------  
[2] Region에서 환자의 주소에 해당하는 좌표와 병원의 좌표를 비교해 가장 가까운 곳에 배치.  
    capacity가 가득 찼으면 그 다음으로 가까운 병원 배치.      
    **Python**  
    Dictionary 생성  
    h_capacity[hospital_id] = (capacity, current)  
    : 병원 별 총 수용 인원과 현재 수용인원  
    position[(province,city)] = hospital_id  
    : 중복되는 province,city가 많으니 한 번 구한 가장 가까운 병원을 기억하기 위해 생성.  
    
    
    - "select hospital_id,capacity,current from HOSPITAL"  
      병원의 수용인원, 현재 수를 받아와  
      h_capacity dictionary 초기화.    
      
    - "select patient_id,province,city from PATIENT_INFO"  
      환자별 id, province, city를 받아옴.  
      city = 'etc' or city = NULL 인 경우 city 와 province를 동일하게 해 province의 대표 좌표를 사용.  
      "select success from (select EXISTS (select * from REGION where province = '%s' and city='%s') as success)s" % (province, city)  
      Region table에 없는 province,city 가 있기 때문에  
      IF Region table 내에 있다면 계속 진행 else 마찬가지로 city 와 province을 동일하게 함.    
      
    - 해당하는 province,city에 이미 가장 가까운 병원이 구해져있고( if (province,city) in position ),  
      그 병원에 남은 자리가 있다면 ( if h_capacity[hospital_id][0] > 0 ),  
      sql update문을 통해 환자를 해당 병원에 배치 및 병원의 수용 인원 상태 변경.     
      
    - 병원을 구해야한다면,  
      환자의 주소에 해당하는 좌표와 각 병원들의 좌표를 비교해 가장 가까운 병원을 구한 뒤,  
      sql update문을 통해 환자를 해당 병원에 배치 및 병원의 수용 인원 상태 변경.  
      환자의 주소(province,city)에 해당하는 hospital_id를 position 삽입.  
      
[3] Hospital_id 를 입력하면 해당 병원에 입원해있는 환자 수와 환자 출력 및 환자 정보에서 Hospital_id 클릭 시, 병원의 Google Map 출력  
    - Hospital_id 를 입력하지 않을 경우, 전체 환자 출력
      
    
      

