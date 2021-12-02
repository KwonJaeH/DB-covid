<?php
	require_once 'dbconfig.php';
?>
<!DOCTYPE html>
<html lang="ko">
<head>
<title>구글지도사용하기</title>
<meta charset = 'utf-8'>
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="viewport" content="width=device-width, initial-scale=1">
<script type="text/javascript" src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
<script type="text/javascript" src="http://maps.google.com/maps/api/js?key=AIzaSyCay9SW0eUkdWNKCuveffCvRfNtEMf65nI" >//키를 발급받아 사용하세요</script>
<style>
#map_ma {width:100%; height:400px; clear:both; border:solid 1px red;}
</style>
</head>
<body>
    <?php
        $id = $_GET['hospital_id'];

        $sql = "select name,province,city,latitude,longitude from HOSPITAL where hospital_id = '$id'";
        $result = mysqli_query($con,$sql);
        $data = mysqli_fetch_assoc($result);
        
        $name = $data['name'];
        $province = $data['province'];
        $city = $data['city'];
        $latitude = $data['latitude'];
        $longitude = $data['longitude'];
    ?>

<div id="map_ma"></div>
<script type="text/javascript">

    var name = "<?php echo $name;?>";    
    var province = "<?php echo $province;?>";
    var city = "<?php echo $city;?>";
    var latitude = "<?php echo $latitude;?>";
    var longitude = "<?php echo $longitude;?>";

      $(document).ready(function() {
         var myLatlng = new google.maps.LatLng(latitude,longitude); // 위치값 위도 경도
   var Y_point         = latitude;      // Y 좌표
   var X_point         = longitude;      // X 좌표
   var zoomLevel      = 18;            // 지도의 확대 레벨 : 숫자가 클수록 확대정도가 큼
   var markerTitle      = province    // 현재 위치 마커에 마우스를 오버을때 나타나는 정보
   var markerMaxWidth   = 300;            // 마커를 클릭했을때 나타나는 말풍선의 최대 크기

// 말풍선 내용
   var contentString   = '<div>' +
   '<h2>'+province+'</h2>'+'<h3>'+city+'</h3>'+
   '<p>'+name+'</p>' +
   
   '</div>';
   var myLatlng = new google.maps.LatLng(Y_point, X_point);
   var mapOptions = {
                  zoom: zoomLevel,
                  center: myLatlng,
                  mapTypeId: google.maps.MapTypeId.ROADMAP
               }
   var map = new google.maps.Map(document.getElementById('map_ma'), mapOptions);
   var marker = new google.maps.Marker({
                                 position: myLatlng,
                                 map: map,
                                 title: markerTitle
   });
   var infowindow = new google.maps.InfoWindow(
                                    {
                                       content: contentString,
                                       maxWizzzdth: markerMaxWidth
                                    }
         );
   google.maps.event.addListener(marker, 'click', function() {
      infowindow.open(map, marker);
   });
});
      </script>
</body>
</html>