
# Case table filtering

- 입력 받은 확진자 수 이상 감염된 국내 case 출력.  
  : 입력 받지 않을 때는 default 값은 0 으로 설정.  
    국내 감염 case 이므로, 외국에서의 감염 case(province가 NULL)는 출력에서 제외.
    
# Patient table filtering

- 기간(start date - end date)을 입력 받아 그 기간 동안에 감염된 patient 출력.  
  : 시작 날짜와 끝 날짜의 default 값은 patient table의  
    가장 작은 confirmed_date 2020-01-20 , 가장 큰 confirmed_date 2020-06-30 으로 설정.
    
# Weather table filtering

- Date 와 province 를 입력 받아 해당 wdate, province 의 weather  출력.  
  : 아무 입력 받지않은 처음 페이지에는 모든 날짜, 모든 province의 weather 출력.  
      
    default 값은 province 는 '모두' , wdate = ''   
    
    입력 경우 **4가지** 고려
    
    [1] province 입력 o , wdate 입력 o   
       : 해당하는 날짜에 해당하는 province weather 출력  
         ex) "2020-06-30 'Seoul' - Weather table (Currently xxx weather in databases)"  
    
    [2] province 입력 o , 날짜 입력 x  
       : 날짜 상관없이 해당하는 province 모든 weather 출력  
         ex) "All the weather in 'Seoul' - Weather table (Currently xxx weather in databases)"
    
    [3] province 입력 x , 날짜 입력 o  
       : 해당하는 날짜에 모든 province weather 출력  
         ex) "2020-06-30 All the weather - Weather table (Currently xxx weather in databases)"  
         
    [4] province 입력 x , 날짜 입력 x  
       : 모든 weather 출력  
         ex) "Weather table (Currently 2551 weather in databases)"
         
    
