
# View-Monthly number of Region

'월' 을 입력 받아 해당하는 월에 지역별 확진, 완치, 사망, 누적 확진, 누적 완치, 누적 사망 수를 출력함.  
      
        
- View 생성 및 조회 과정
    
  MONTHLY 뒤에 나오는 C,R,D,ACCUM 은 Confirmed, Released, Decreased, Accumulated 를 의미함  
     
    
  [1] 새로운 view를 생성하기 때문에 기존의 이름이 같은 view가 있으면 drop(삭제) 해준다.    
  
  
  [2] Patient table 을 조회, 해당하는 '월'의 지역별 **확진** 수를 저장하는 view 생성 (MONTHLY_C)  
  [3] Patient table 을 조회, 해당하는 '월'의 지역별 **완치** 수를 저장하는 view 생성 (MONTHLY_R)  
  [4] Patient table 을 조회, 해당하는 '월'의 지역별 **사망** 수를 저장하는 view 생성 (MONTHLY_D)  
  [5] Patient table 의 존재 이유는 "확진"이므로 confirmed_date 를 기준으로 조회한 MONTHLY_C 에 MONTHLY_R 를 left join 하여  
  **확진 + 완치** 수를 저장하는 view 생성 (MONTHLY_CR) 
     
     
  [6] MONTHLY_CR 에 MONTHLY_D 를 left join 하여 **확진 + 완치 + 사망** 수를 저장하는 view 생성 (MONTHLY_CRD) 
  
  
    
  [7] TIME_PROVINCE table에 날짜별로 저장된 지역의 누적 확진, 누적 완치, 누적 사망수를 조회,  
      해당하는 '월'의 지역별 max(누적 확진), max(누적 완치), max(누적 사망) 을 사용하여  
      해당하는 '월'의 **누적 확진 + 누적 완치 + 누적 사망** 수를 저장하는 view 생성 (MONTHLY_ACCUM)
      
      
  [8] 최종적으로 MONTHLY_CRD 와 MONTHLY_ACCUM 을 province 기준 join 하여  
      **확,완,사 + 누확,누완,누사** 수를 저장하는 view 생성 (MONTHLY)  
      
      
  [9] MONTHLY 를 Province 오름차순으로 select 하여 조회 하여 출력.
